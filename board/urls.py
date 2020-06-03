from django.contrib import admin
from django.urls import path
from .views import home

from .views import post_write
urlpatterns = [
    path('',home, name = "home"),
    path('write/',post_write, name='write'),
]
