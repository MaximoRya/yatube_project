# posts/urls.py
from django.urls import  include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug_any>/', views.group_posts)
] 