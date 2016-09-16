"""Test flight_paths.py."""

import pytest


AIRPORT_KEYS = ['city', 'destination_cities', 'lat_lon', 'airport']


@pytest.fixture(scope='session')
def airport_info():
    """Test get_airports returns a list of dicts."""
    from .flight_paths import get_airports
    return get_airports()


@pytest.fixture
def fake_airports():
    return [dict(
        city='purgatory',
        airport='purgatory',
        destination_airports=['hell', 'heaven'],
        lat_lon=[0, 0]
    ), dict(
        city='hell',
        airport='hell',
        destination_airports=['heaven', 'purgatory'],
        lat_lon=[-666, -666]
    ), dict(
        city='heaven',
        airport='heaven',
        destination_airports=[],
        lat_lon=[7, 7]
    ), dict(
        city='my house',
        airport='my house',
        destination_airports=[],
        lat_lon=[float('inf'), float('inf')]
    )]


@pytest.mark.parametrize('key', AIRPORT_KEYS)
def test_airports_have_keys(airport_info, key):
    """Test airports have necessary keys."""
    assert all(map(lambda c: key in c, airport_info))


def test_flight_path_make_graph(airport_info):
    from .flight_paths import make_airport_graph
    """Test graph """
    assert len(make_airport_graph(airport_info).nodes())


def test_get_airports_in_city():
    """Test get_airports_in_city."""
    from .flight_paths import get_airports_in_city
    airports = [dict(city='a'), dict(city='b'), dict(city='a')]
    assert len(list(get_airports_in_city('a', airports))) == 2


def test_get_city_from_airport():
    """Test get_city_from_airport."""
    from .flight_paths import get_city_from_airport
    airports = [dict(city='quux', airport='a')]
    assert get_city_from_airport('a', airports) == 'quux'


def test_shortest_distance_path(fake_airports):
    """Test shortest distance path."""
    from .flight_paths import shortest_distance
    path, distance = shortest_distance('purgatory', 'heaven', fake_airports)
    assert 'hell' not in path


def test_shortest_distance_distance(fake_airports):
    """Test shortest distance distance."""
    from .flight_paths import shortest_distance
    path, distance = shortest_distance('purgatory', 'heaven', fake_airports)
    assert distance < 1000


def test_shortest_distance_no_path(fake_airports):
    """Test shortest distance raises error when given unconnected airports."""
    from .flight_paths import shortest_distance
    with pytest.raises(ValueError):
        print(shortest_distance('hell', 'my house', fake_airports))
