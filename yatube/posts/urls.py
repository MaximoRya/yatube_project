# posts/urls.py
from django.urls import  include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:any_slug>/', views.group_posts)
] 