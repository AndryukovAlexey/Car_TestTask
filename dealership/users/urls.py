from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('reg/', views.registr, name='reg-page'),
    path('auth/', views.Auth.as_view(), name='auth-page'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]