from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_form.html',
                  {'form': form})

def ingredient_create(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = IngredientForm()

    return render(request, 'recipes/ingredient_form.html',
                  {'form': form, 'recipe': recipe})

