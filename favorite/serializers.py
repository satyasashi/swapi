"""
This file contains the Serializers for our Favorite app
Which takes in the data and serializes python objects into JSON
and deserializes JSON into python data types.
"""
from rest_framework import serializers
from .models import Movie, Planet


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ('name',)
