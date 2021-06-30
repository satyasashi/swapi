from django.db import models

# Create your models here.


class Movie(models.Model):
    """This is a basic model that holds movie title"""
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Planet(models.Model):
    """This model holds the names of Planet"""
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
