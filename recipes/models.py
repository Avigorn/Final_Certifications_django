from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Ингридиенты')
    steps_cooking = models.TextField(verbose_name='Этапы приготовления')
    time_for_cooking = models.IntegerField(default=10, verbose_name='Время приготовления')
    image = models.ImageField(verbose_name='Фото рецепта')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', kwargs={'pk': self.pk})
