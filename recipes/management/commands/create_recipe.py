from django.core.management import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    """
    Create recipes
    """
    def handle(self, *args, **options):
        self.stdout.write("Create recipes")

        recipes_names = [

        ]
        for recipe_name in recipes_names:
            recipe, created = Recipe.objects.get_or_create(title=recipes_names)
            self.stdout.write(f'Recipe created {recipe.title}')


        self.stdout.write(self.style.SUCCESS('Recipes created successfully'))