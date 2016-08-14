from __future__ import division

def series_sum(n):
    return '{0:.2f}'.format(sum(1/(1 + i*3) for i in range(n)))
