from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car, Comment
from .serializers import CarSerializerG, CommentSerializerG, CarSerializerPP, CommentSerializerP


class CarAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializerG
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def post(self, request):
        request.POST._mutable = True
        request.data['owner_id'] = request.user.id
        request.POST._mutable = True
        serializer = CarSerializerPP(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'car': serializer.data})

class CarAPIViewDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        return Response({'car': CarSerializerG(car, many=False).data})
        
    def put(self, request, pk):
        car = Car.objects.get(id=pk)
        if request.user == car.owner:
            request.POST._mutable = True
            request.data['owner_id'] = request.user.id
            request.POST._mutable = True
            serializer = CarSerializerPP(data=request.data, instance=car)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'car': serializer.data})
        return Response({'error': 'only owner can change this!'})
    
    def delete(self, request, pk):
        car = Car.objects.get(id=pk)
        if request.user == car.owner:
            car.delete()
            return Response({'success': "Car was deleted!"})
        return Response({'error': 'only owner can delete this!'})

class CommentsAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        comments = Comment.objects.filter(car_id=pk)
        return Response({'comments': CommentSerializerG(comments, many=True).data})
    
    def post(self, request, pk):
        request.POST._mutable = True
        request.data['author_id'] = request.user.id
        request.data['car_id'] = pk
        request.POST._mutable = True
        serializer = CommentSerializerP(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'comments': serializer.data})

