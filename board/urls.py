from django.contrib import admin
from django.urls import path
from .views import home,post_write,post_search

urlpatterns = [
    path('',home, name = "home"),
    path('write/', post_write, name='write'),
    path('search/', post_search, name='search'),
]
