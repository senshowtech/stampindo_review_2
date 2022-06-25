from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField()


class Ingredient(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ingredients",)
    protein = models.FloatField()
    carb = models.FloatField()
    fat = models.FloatField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    release_date = models.DateField()


class Author(models.Model):
    books = models.ManyToManyField('Book', related_name='authors', blank=True)
    name = models.CharField(max_length=225)
    biography = models.TextField()
