from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Car, Comment
from .forms import NewCar, NewComment


class HomePage(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Список авто'
        return ctx

class CarPage(DetailView):
    model = Car
    template_name = 'cars/detail.html'
    context_object_name = 'car'

    def post(self, request, pk):
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.car = Car.objects.get(id=pk)
            comment.save()
            return redirect(request.path_info)
        else:
            return form

    def get_context_data(self, **kwargs):
        ctx = super(CarPage, self).get_context_data(**kwargs)
        ctx['comments'] = Comment.objects.filter(car=self.get_object())
        return ctx

@login_required
def add_car(request):
    if request.method == 'POST':
        form = NewCar(request.POST)   
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('/')
    else:
        form = NewCar()
    return render(request, 'cars/add_car.html', {'form': form})

def change_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.user == car.owner:
        if request.method == 'POST':
            form = NewCar(request.POST, instance=car)
            if form.is_valid():
                car_form = form.save(commit=False)
                car_form.owner = request.user
                car_form.save()
                return redirect('car-page', pk)
        else:
            form = NewCar(instance=car)
    else:
        return redirect('/')
    return render(request, 'cars/change.html', {'form':form, 'car':car})

def delete_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.user == car.owner:
        car.delete()
        return redirect('/')
    else:
        return redirect('/')


