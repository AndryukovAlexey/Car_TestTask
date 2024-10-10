from rest_framework import serializers
from .models import Car, Comment


class CarSerializerPP(serializers.Serializer):
    make = serializers.CharField(max_length=70)
    model = serializers.CharField(max_length=70)
    year = serializers.IntegerField()
    description = serializers.CharField()
    owner_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.make = validated_data.get("make", instance.make)
        instance.model = validated_data.get("model", instance.model)
        instance.year = validated_data.get("year", instance.year)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

class CarSerializerG(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner_id')

class CommentSerializerG(serializers.ModelSerializer):
    class Meta:
            model = Comment
            fields = ("content", 'created_at', 'author_id')

class CommentSerializerP(serializers.Serializer):
    content = serializers.CharField()
    author_id = serializers.IntegerField()
    car_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
