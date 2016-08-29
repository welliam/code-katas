from .data_structures.priority_queue import PriorityQueue


card_ord = 'A23456789TJQK'


def deck_sort(t):
    """Sort cards using priority queue.

    Ace = A, 10=T, Joker=J, Queen=Q, King=K.
    """
    pq = PriorityQueue()
    for c in t:
        pq.insert(c, card_ord.find(c))
    result = []
    for _ in t:
        result.append(pq.pop())
    return result


def deck_sort2(t):
    """Sort as if input were a deck of cards

    Ace = A, 10=T, Joker=J, Queen=Q, King=K.
    """
    return list(sorted(t, key=card_ord.find))
