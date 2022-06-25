from django.db import models

# Create your models here.


class Query(models.Model):
    int = models.IntegerField(max_length=100)
    char = models.CharField(max_length=100)
    desimal = models.FloatField()
    text = models.TextField()
