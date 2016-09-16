import json


AIRPORTS_FILE = 'static/cities_with_airports.json'

def get_flight_paths(filename=AIRPORTS_FILE):
    """Get flight path info."""
    return json.load(open(filename))
