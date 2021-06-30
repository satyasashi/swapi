import json
from django.http import response

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Movie, Planet
from .serializers import MovieSerializer, PlanetSerializer


class AddMovieTestCase(APITestCase):
    """This tests if we can Add a 'Movie' to our DB."""

    def test_add_movie(self):
        data = {"title": "Interstellar"}
        response = self.client.post("/movies/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AddPlanetTestCase(APITestCase):
    """This tests if we can Add a 'Movie' to our DB."""

    def test_add_planet(self):
        data = {"name": "Mars"}
        response = self.client.post("/planets/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SearchPlanetTestCase(APITestCase):
    """This test will search for a 'Planet' that doesn't exist
    and expected to throw 400 Bad Request"""

    def test_search_planet(self):
        planet_name = "XV11-MN-O5"
        response = self.client.get("/planets/search/{}/".format(planet_name))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
