from .data_structures.trie import Trie
from itertools import islice


class AutoCompleter(object):
    """Object instantiated with a vocabulary used for autocompletion."""

    def __init__(self, to_fill, max_completions=5):
        """Creates a vocabulary, sets the max number of completions."""
        self.trie = Trie()
        for value in to_fill:
            self.trie.insert(value)
        self.max_completions = max_completions

    def __call__(self, start):
        """Autocomplete a word."""
        return list(islice(self.trie.traverse_at(start), self.max_completions))
