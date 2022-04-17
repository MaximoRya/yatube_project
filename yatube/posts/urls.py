# posts/urls.py
from django.urls import  include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/<int:pk>/', views.group_posts)
] 