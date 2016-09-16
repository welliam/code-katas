"""Test flight_paths.py."""

import pytest


CITY_KEYS = ['city', 'destination_cities', 'lat_lon']


@pytest.fixture(scope='session')
def flight_path_info():
    from flight_paths import get_flight_paths
    return get_flight_paths()


@pytest.mark.parametrize('key', CITY_KEYS)
def test_flight_paths_have_keys(flight_path_info, key):
    assert all(map(lambda c: key in c, flight_path_info))
