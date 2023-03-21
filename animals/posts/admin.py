from django.contrib import admin

from .models import *


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'slug')


class KingOfAnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


admin.site.register(KindOfAnimal, KingOfAnimalAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Animal, AnimalAdmin)
