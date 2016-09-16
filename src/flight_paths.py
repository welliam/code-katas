import json
from data_structures.graph import Graph
from calculate_distance import calculate_distance


AIRPORTS_FILE = 'static/cities_with_airports.json'


def get_airports(filename=AIRPORTS_FILE):
    """Get flight path info."""
    return json.load(open(filename))


def make_airport_graph(airports):
    """From a dict of flight paths, generate a graph."""
    g = Graph()
    airport_dict = {airport['airport']: airport for airport in airports}
    for airport in airports:
        for destination_airport in airport['destination_airports']:
            try:
                distance = calculate_distance(
                    airport['lat_lon'],
                    airport_dict[destination_airport]['lat_lon']
                )
                g.add_edge(airport['airport'], destination_airport, distance)
            except KeyError:
                pass
    return g


def get_airports_in_city(city, airports):
    """Get all airports in a city."""
    return filter(lambda c: c['city'] == city, airports)


def get_city_from_airport(airport, airports):
    """Get city airport is in."""
    return [a for a in airports if a['airport'] == airport][0]['city']


def shortest_distance(c1, c2, airports=get_airports()):
    """Return the shortest flight between two airports."""
    g = make_airport_graph(airports)
    distance, path = min([
        g.shortest_path(a1['airport'], a2['airport'])[::-1]
        for a1 in get_airports_in_city(c1, airports)
        for a2 in get_airports_in_city(c2, airports)
    ])
    return ([get_city_from_airport(a, airports) for a in path], distance)
