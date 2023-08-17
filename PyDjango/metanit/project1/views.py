from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Получить HttpRequest — параметр запроса
    # Выполнить операции, используя информацию из запроса.
    # Вернуть HttpResponseH
    return HttpResponse("Hello from Django")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("Контакты")

def lesson_4(request):
    return HttpResponse('Домашка по 4 занятию')
# Create your views here.
