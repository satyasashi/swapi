from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    MoviesList,
    PlanetsList,
    ApiRoot,
    SearchPlanet
)

urlpatterns = format_suffix_patterns([
    path('', ApiRoot.as_view(), name='api-root'),
    path('movies/', MoviesList.as_view(), name="movies-list"),
    path('planets/', PlanetsList.as_view(), name="planets-list"),
    re_path('planets/search/(?P<name>[\w\d-]+)/',
            SearchPlanet.as_view(), name="search-planet"),
])
