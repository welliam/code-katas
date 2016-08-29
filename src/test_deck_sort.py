import pytest

INPUTS = [  # some from code-katas
    ('39A5T824Q7J6K', 'A23456789TJQK'),
    ('Q286JK395A47T', 'A23456789TJQK'),
    ('54TQKJ69327A8', 'A23456789TJQK'),
    ('', ''),
    ('2', '2')
]


@pytest.mark.parametrize('unsorted_deck, sorted_deck', INPUTS)
def test_deck_sort(unsorted_deck, sorted_deck):
    from deck_sort import deck_sort
    assert deck_sort(list(unsorted_deck)) == list(sorted_deck)


@pytest.mark.parametrize('unsorted_deck, sorted_deck', INPUTS)
def test_deck_sort2(unsorted_deck, sorted_deck):
    from deck_sort import deck_sort2
    assert deck_sort2(list(unsorted_deck)) == list(sorted_deck)
