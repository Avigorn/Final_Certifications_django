from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models
from django.shortcuts import render

from .models import Recipe


def start(request):
    latest_recipes = Recipe.objects.order_by('-image')[:3]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'Final_Certifications_django/base.html', context)

def home(request):
    recipes = models.Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/home.html', context)



class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeDetail(DetailView):
    model = models.Recipe


class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes:home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', "steps_cooking", "time_for_cooking", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return redirect(self.get_success_url())


    def get_success_url(self):
        return reverse('recipes:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', "steps_cooking", "image"]

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



