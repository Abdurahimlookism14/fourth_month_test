from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, choices=[('г', 'г'), ('кг', 'кг'), ('мл', 'мл'),
                                                      ('л', 'л'), ('шт', 'шт')])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"
