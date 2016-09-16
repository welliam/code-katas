"""Test sum of the first nth terms kata"""

import pytest

SUM_TERMS_TABLE = [
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39")
]


@pytest.mark.parametrize('n, terms_sum', SUM_TERMS_TABLE)
def test_max_size(n, terms_sum):
    """Test sum of the first nth terms kata"""
    from .sum_terms import series_sum
    assert series_sum(n) == terms_sum
