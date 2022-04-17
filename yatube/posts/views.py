from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(f'Поехали...')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, num):
    return HttpResponse(f'Мороженое номер {num}')
    