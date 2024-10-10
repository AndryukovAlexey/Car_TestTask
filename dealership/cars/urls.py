from django.urls import path
from . import views
from . import apiview


urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('car/<int:pk>', views.CarPage.as_view(), name='car-page'),
    path('add_car/', views.add_car, name='add_car-page'),
    path('change_car/<int:pk>', views.change_car, name='change_car-page'),
    path('delete_car/<int:pk>', views.delete_car, name='delete_car-page'),
    path('api/cars/', apiview.CarAPIView.as_view()),
    path('api/cars/<int:pk>/', apiview.CarAPIViewDetail.as_view()),
    path('api/cars/<int:pk>/comments/', apiview.CommentsAPIView.as_view()),
]