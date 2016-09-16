"""Test flight_paths.py."""

import pytest


CITY_KEYS = ['city', 'destination_cities', 'lat_lon']


@pytest.mark.parametrize('key', CITY_KEYS)
def test_flight_paths_have_keys(key):
    from flight_paths import get_flight_paths
    assert all(map(lambda c: key in c, get_flight_paths()))
