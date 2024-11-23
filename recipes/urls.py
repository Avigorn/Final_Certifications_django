from django.urls import path

from recipes import views



app_name = "recipes"
urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:pk>', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipe_create"),
    path('recipe/<int:pk>/update', views.RecipeUpdate.as_view(), name="recipe_update"),
    path('recipe/<int:pk>/delete', views.RecipeDelete.as_view(), name="recipe_delete"),
]