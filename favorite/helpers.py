from .models import Planet


def get_planets(name):
    filtered_data = Planet.objects.filter(name__icontains=name)
    if filtered_data.count() > 0:
        planet_objs = [{"name": p.name} for p in filtered_data]
        return planet_objs
    else:
        return None


def raw_data_from_response(response_object, category):
    if category == "planets":
        result = [{"name": p["name"]}
                  for indx, p in enumerate(response_object["results"])]
    else:
        result = [{"title": m["title"]}
                  for indx, m in enumerate(response_object["results"])]

    return result
