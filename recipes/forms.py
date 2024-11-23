from django import forms
from django.contrib.auth.models import User


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    steps_cooking = forms.CharField(widget=forms.Textarea)
    time_for_cooking = forms.IntegerField()
    photo = forms.ImageField()
    author = forms.ModelChoiceField(queryset=User.objects.all())
