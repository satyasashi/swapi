# Consuming SWAPI using DRF

This Application contains few endpoints that consume the SWAPI (https://swapi.dev/). Following are the basic operations you can perform:

1. List of endpoints available to use
2. Ability to add new Movie/Planet to the storage
3. Listing the Movies/Planets by fetching from SWAPI & storage used
4. Searching/Filtering by Planets

## Installation

Firstly, open your terminal or command prompt and clone this repository.

`$ git clone https://github.com/satyasashi/spotdraft-swapi.git`

Create a virtual environment

`$ python -m venv swapienv`

Activate the environment

`$ source swapienv/bin/activate`

Install dependencies by moving to project path.

`$ cd spotdraft-swapi && pip install -r requirements.txt`

Do the initial migrations

`$ python manage.py migrate`

## Run Tests

Before we begin our usage, you can run automated tests for this application by using following command. This will run tests listed in `favorite/tests.py` module.

```
(swapienv)$: python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.888s

OK
Destroying test database for alias 'default'...
```

The 3 tests it ran are for operations such as "Adding Movie", "Adding Planet" and "Search" which interacts with SWAPI and DB.

## Basic Usage

To use the endpoints in this application, navigate to: (http://localhost:8000/)

### Available Endpoints | API ROOT

You will see API ROOT which shows the list of endpoints available in this application like below.

OR

You can also use terminal to call these endpoints using utilities like `http`, `curl` etc,.

```
(swapienv)$ http http://localhost:8000
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 85
Content-Type: application/json
Date: Wed, 30 Jun 2021 19:43:00 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "movies": "http://localhost:8000/movies/",
    "planets": "http://localhost:8000/planets/"
}

```

### Movie List

You can click on any endpoint to see list of Movies. These movies are fetched from (http://localhost:8000/movies/) and also it does get all the movies
that are saved in our storage. The result will be joined together to show the data in JSON format as a API response.

Here is the sample output

```
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 217
Content-Type: application/json
Date: Wed, 30 Jun 2021 19:44:27 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "title": "A New Hope"
    },
    {
        "title": "The Empire Strikes Back"
    },
    {
        "title": "Return of the Jedi"
    },
    {
        "title": "The Phantom Menace"
    },
    {
        "title": "Attack of the Clones"
    },
    {
        "title": "Revenge of the Sith"
    }
]
```

### Planets List

You can click on any endpoint to see list of Planets. These planets are fetched from (http://localhost:8000/planets/) and also it does get all the planets
that are saved in our storage. The result will be joined together to show the data in JSON format as a API response.

Here is the sample output:

```
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 217
Content-Type: application/json
Date: Wed, 30 Jun 2021 19:47:18 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "name": "Tatooine"
    },
    {
        "name": "Alderaan"
    },
    {
        "name": "Yavin IV"
    },
    {
        "name": "Hoth"
    },
    {
        "name": "Dagobah"
    },
    {
        "name": "Bespin"
    },
    {
        "name": "Endor"
    },
    {
        "name": "Naboo"
    },
    {
        "name": "Coruscant"
    },
    {
        "name": "Kamino"
    }
]

```

### Adding Movie

Movie should have a `title`. So when passing data, you should pass the `title` as your argument. If not, it will throw `This field is required` for that field.

```
(swapienv)$: http --form http://localhost:8000/movies/ title='Interstellar'
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 19
Content-Type: application/json
Date: Wed, 30 Jun 2021 19:52:09 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "title": "Interstellar"
}
```

### Adding Planet

Planet should have a `name`. So when passing data, you should pass the `name` as your argument. If not, it will throw `This field is required` for that field.

```
(swapienv)$: http --form http://localhost:8000/planets/ name='XVHI'
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 19
Content-Type: application/json
Date: Wed, 30 Jun 2021 19:52:09 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "name": "XVHI"
}
```

Accessing the Movie/Planet endpoints now should be showing the information from both SWAPI & our storage.
