import requests
import pprint
import json

from requests.api import get
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import MovieSerializer, PlanetSerializer
from .models import Movie, Planet
from .helpers import get_planets, raw_data_from_response


class MoviesList(APIView):
    """Lists all the movies from SWAPI"""

    def get(self, request, format=None):
        """ 
        using 'requests' library, fetch the JSON data from SWAPI
        now return the response as JSON.
        """
        movies_response = requests.get('https://swapi.dev/api/films/')
        movies_response = movies_response.json()
        raw_data = raw_data_from_response(movies_response, "movies")

        # get all the movies we have in our storage if any and combine the results.
        db_movies = [{"title": m.title} for m in Movie.objects.all()]
        final_movies = raw_data+db_movies
        return Response(final_movies)

    def post(self, request, format=None):
        """
        Takes in a 'title' as data. If serialized
        successfully, saves in DB.
        """
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            # if the data serialized successfully, then save it.
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetsList(APIView):
    """Lists all the plantes from SWAPI"""

    def get(self, request, format=None):
        """ Using 'requests' library, fetch the JSON data from SWAPI
        now return the response as JSON. """

        planets_response = requests.get('https://swapi.dev/api/planets/')
        planets_response = planets_response.json()
        raw_data = raw_data_from_response(planets_response, "planets")

        # get all the planets we have in our storage if any and combine the results.
        db_planets = [{"name": p.name} for p in Planet.objects.all()]
        final_planets = raw_data+db_planets

        return Response(final_planets)

    def post(self, request, format=None):
        """ Takes in a 'name' as data. If serialized
        successfully, saves in DB. """

        planet_serializer = PlanetSerializer(data=request.data)
        if planet_serializer.is_valid():
            # if the data serialized successfully, then save it.
            planet_serializer.save()
            return Response(planet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(planet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchPlanet(APIView):
    """Takes in the 'name' of a planet as argument and returns the 
    result if exist or empty results if not found."""

    def get(self, request, name, format=None):
        # Fetch SWAPI JSON data.
        get_planet_response = requests.get(
            'https://swapi.dev/api/planets/?search={}'.format(name))
        get_planet_response = get_planet_response.json()
        planet_objs = get_planets(name) if get_planets(name) else None

        if len(get_planet_response["results"]) == 0:
            # If SWAPI doesn't have the planet results,
            # check and return planets if any from our DB.
            if planet_objs:
                return Response(planet_objs)
            else:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # join both values from SWAPI and our DB
            raw_data = [{"name": p["name"]}
                        for indx, p in enumerate(get_planet_response["results"])]
            if planet_objs:
                raw_data = raw_data+planet_objs

            return Response(raw_data)


class ApiRoot(APIView):
    """Acts as Home page of the API containing 'Movies' & 'Planets' List endpoints"""

    def get(self, request, format=None):
        return Response({
            'movies': reverse('movies-list', request=request, format=format),
            'planets': reverse('planets-list', request=request, format=format)
        })
