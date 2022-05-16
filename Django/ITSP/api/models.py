from operator import mod
from tokenize import Name
from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    Name = models.CharField(max_length=200)
    Member1 = models.CharField(max_length=200)
    Member2 = models.CharField(max_length=200)
    Member3 = models.CharField(max_length=200)
    Member4 = models.CharField(max_length=200)

    def __str__(self):
        return self.id