from django.db import models
from django.core.urlresolvers import reverse


# Create your models here. where the data 4 the classes on this page will go
#classes go here

#pk/id 1
class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=150)
    recipeImage = models.FileField()
    courseType = models.CharField(max_length=30)
    mealType = models.CharField(max_length=30)
    ingredients = models.TextField(max_length=20000)
    directions = models.TextField(max_length=10000)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.recipeTitle + " - " + self.mealType + " - " + self.courseType


#class CourseType(models.Model):
#    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
##class Ingredient(models.Model):
##    recipeList = models.ForeignKey(Recipe, on_delete=models.CASCADE)
##    ingredients = models.CharField(max_length=25)

##    def __str__(self):
##        return self.ingredients