"""Solve sum of nth terms exercise from code katas.
http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python
"""

from __future__ import division


def series_sum(n):
    """The sum of the first n terms in the series [1, 1/4, 1/7 ...],
    to two decimal points. Return a string
    """
    return '{0:.2f}'.format(sum(1/(1 + i*3) for i in range(n)))
