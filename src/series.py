

def fibonacci(n):
    """Return nth number of fibonacci sequence"""
    if n <= 0:
        return 0
    l = [0, 1]
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[n-1]


def lucas(n):
    """Return nth number of lucas series"""
    if n <= 0:
        return 0
    l = [2, 1]
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[n-1]


def sum_series(n, first=0, second=1):
    """Return nth number of a sequence with the first two digits x and y.
    Defaults to fibonacci sequence otherwise."""
    if n <= 1:
        return first
    else:
        return sum_series(n-1, second, first + second)


if __name__ == '__main__':
    print(u"""
    This module defines functions that implement mathematical series.
    ...
    fibonacci(n):

    {}
    {}
    {}
    ...
    lucas(n):

    {}
    {}
    {}
    ...
    sum_series(n[,First Number, Second Number])

    {}
    {}
    {}
    """).format(fibonacci.__doc__, u'>>> fibonacci(3)', fibonacci(3),
                lucas.__doc__, u'>>> lucas(3)', lucas(3),
                sum_series.__doc__, u'>>> sum_series(3, 4, 4)',
                sum_series(3, 4, 4))
