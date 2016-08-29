from data_structures.priority_queue import PriorityQueue


card_ord = 'A23456789TJQK'


def deck_sort(t):
    pq = PriorityQueue()
    for c in t:
        pq.insert(c, card_ord.find(c))
    result = []
    for _ in t:
        result.append(pq.pop())
    return result
