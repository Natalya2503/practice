from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Задача 1',
        'title1': 'Задача 2',
        'description': 'Описание задачи',
        'status': 'Выполнена',
        'status1': 'Не выполнена'
    }
    return render(request, 'task_list.html', context=data)

def details(request, task_id):
    data = {
        'title': 'Задача №1',
        'description': 'Описание задачи',
        'status': 'выполнена',
       
    }
    return render(request, 'task_detail.html', context=data)





