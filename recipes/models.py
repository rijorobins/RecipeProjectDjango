from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=120)
    category = models.CharField(max_length=100)
    recipe_image = models.ImageField(upload_to="images")
    created_by = models.CharField(max_length=120)

    def __str__(self):
        return int(self.recipe_name)