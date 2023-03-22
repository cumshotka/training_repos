from django.db import models


class KindOfAnimals(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Виды животных'


class Animals(models.Model):
    title = models.CharField(max_length=30)
    kind = models.ForeignKey(KindOfAnimals, on_delete=models.CASCADE)
    description = models.TextField()
    color = models.CharField(max_length=50)
    lifetime = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'
