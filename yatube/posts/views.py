from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f'Поехали...')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
    