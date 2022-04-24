from django.shortcuts import render
from django.http import HttpResponse





def index(request):
    template = 'posts/index.html'
    title = 'СОцСЕТь'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context) 

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request):
    template = 'posts/group_list.html'
    title = "Группы"
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)
    