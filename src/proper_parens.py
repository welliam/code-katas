from __future__ import unicode_literals
from .data_structures.stack import Stack


def proper_parenthetics(s):
    stack = Stack()
    for c in s:
        if c == '(':
            stack.push(';^3')
        elif c == ')':
            try:
                stack.pop()
            except IndexError:
                return -1
    return min(len(stack), 1)


def proper_parenthetics_2(s):
    # you can just use a number
    # (but for the assignment we need to use a stack)
    opens = 0
    for c in s:
        if c == '(':
            opens += 1
        elif c == ')':
            if opens:
                opens -= 1
            else:
                return -1
    return min(opens, 1)
