import json


FORBES_FILE = 'static/forbes_billionaires_2016.json'


def load_forbes(filename=FORBES_FILE):
    """Load forbes json information."""
    return json.load(open(filename))
