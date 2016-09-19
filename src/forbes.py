import json


FORBES_FILE = 'static/forbes_billionaires_2016.json'


def load_forbes(filename=FORBES_FILE):
    """Load forbes json information."""
    return json.load(open(filename))


def oldest_under_80(billionares):
    """Returns the oldest member of billionares under 80."""
    oldest = None
    for b in filter(lambda b: b['age'] < 80, billionares):
        oldest = b if (not oldest or b['age'] > oldest['age']) else oldest
    return oldest


def youngest(billionares):
    """Returns the youngest member of billionares."""
    youngest = None
    for b in filter(lambda b: b['age'] > -1, billionares):
        youngest = b if (not youngest or b['age'] < youngest['age']) else youngest
    return youngest
