from django.db import models
from django.contrib.auth.models import User


class KindOfAnimal(models.Model):
    title = models.CharField(
        'Вид животного',
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        'Слаг животного',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.title


class Color(models.Model):
    color = models.CharField(
        'Цвет',
        max_length=50,
        unique=True
    ),
    slug = models.SlugField(
        'Слаг цвета',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.color


class Animal(models.Model):
    name = models.CharField(
        'Кличка',
        max_length=100
    )
    breed = models.CharField(
        'Порода',
        max_length=100,
        unique=True
    ),
    color = models.ForeignKey(
        Color,
        verbose_name='Цвет питомца',
        on_delete=models.SET_NULL,
        null=True,
    )
    kind = models.ForeignKey(
        KindOfAnimal,
        verbose_name='Порода питомца',
        on_delete=models.CASCADE
    )
    old = models.IntegerField(
        'Возраст питомца'
    )
    lifetime = models.IntegerField(
        'Среднее время жизни',
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Хозяин питомца',
        on_delete=models.CASCADE
    )
