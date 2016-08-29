import pytest

INPUTS = [  # some from code-katas
    ('39A5T824Q7J6K', 'A23456789TJQK'),
    ('Q286JK395A47T', 'A23456789TJQK'),
    ('54TQKJ69327A8', '54TQKJ69327A8'),
    ('', ''),
    ('2', '2')
]


@pytest.mark.parametrize('unsorted_deck, sorted_deck', INPUTS)
def test_deck_sort(unsorted_deck, sorted_deck):
    from sort_cards import sort_cards
    assert sort_cards(list('39A5T824Q7J6K')) == list('A23456789TJQK')
