from django.contrib import admin
from django.urls import path
from .views import register,login,logout,profile,insert


urlpatterns = [
    path('register/', register, name='register'),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout'),
    path('profile/<int:id>',profile,name='profile'),
    path('profile/<int:id>/insert',insert,name='insert'),
]


