import pytest


BILLIONAIRES = [[
    {'age': 79, 'name': 'correct'},
    {'age': 27, 'name': 'incorrect'},
    {'age': 0, 'name': 'incorrect'},
    {'age': 81, 'name': 'incorrect'}
], [
    {'age': 1, 'name': 'correct'},
    {'age': 81, 'name': 'incorrect'}
]]


def test_load_forbes():
    """Test forbes loading function."""
    from .forbes import load_forbes, FORBES_FILE
    assert isinstance(load_forbes(FORBES_FILE), list)


@pytest.mark.parametrize('billionaires', BILLIONAIRES)
def test_oldest_under_80(billionaires):
    """Test youngest returns oldest billionaire under 80."""
    from .forbes import oldest_under_80
    assert oldest_under_80(billionaires)['name'] == 'correct'


def test_youngest():
    """Test youngest returns youngest billionaire with valid age."""
    from .forbes import youngest
    billionaires = [
        {'age': 1, 'name': 'correct'},
        {'age': -1, 'name': 'incorrect'},
        {'age': 2, 'name': 'incorrect'}
    ]
    assert youngest(billionaires)['name'] == 'correct'
