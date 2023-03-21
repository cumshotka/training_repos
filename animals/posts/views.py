from django.shortcuts import render

from .models import *


def index(requests):
    animals = Animals.objects.all()
    context = {
        'title': 'Главная страница',
        'animals': animals
    }
    return render(requests, 'posts/index.html', context)
