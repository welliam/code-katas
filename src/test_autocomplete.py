import pytest
from src.autocomplete import AutoCompleter


VOCABULARY = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']

AUTOCOMPLETE_TABLE = ['f', 'fi', 'fin', 'finally', 'hello', '']


@pytest.mark.parametrize('start', AUTOCOMPLETE_TABLE)
def test_autocomplete(start):
    complete_me = AutoCompleter(VOCABULARY, max_completions=4)
    for value in complete_me(start):
        assert value.startswith(start)


@pytest.mark.parametrize('start', AUTOCOMPLETE_TABLE)
def test_autocomplete_length(start):
    completions = 4
    complete_me = AutoCompleter(VOCABULARY, max_completions=completions)
    assert len(complete_me(start)) <= completions
