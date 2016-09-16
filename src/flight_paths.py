import json
from data_structures.graph import Graph
from calculate_distance import calculate_distance


AIRPORTS_FILE = 'static/cities_with_airports.json'


def get_flight_paths(filename=AIRPORTS_FILE):
    """Get flight path info."""
    return json.load(open(filename))


def make_flight_graph(cities):
    """From a dict of flight paths, generate a graph."""
    g = Graph()
    city_dict = {city['city']: city for city in cities}
    for city in cities:
        for destination_city in city['destination_cities']:
            try:
                distance = calculate_distance(
                    city['lat_lon'], city_dict[destination_city]['lat_lon']
                )
                g.add_edge(city['city'], destination_city, distance)
            except KeyError:
                pass
    return g
