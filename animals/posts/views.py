from django.shortcuts import render

from .models import *


def index(request):
    pets = Animal.objects.all()
    return render(request, 'posts/index.html', {'pets': pets})
