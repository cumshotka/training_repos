from django.shortcuts import render

from .models import *


def index(requests):
    animals = Animals.objects.all()
    category = KindOfAnimals.objects.all()
    context = {
        'title': 'Главная страница',
        'animals': animals,
        'category': category
    }
    return render(requests, 'posts/index.html', context)
