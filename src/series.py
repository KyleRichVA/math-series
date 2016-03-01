

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


def sum_series(n, x=0, y=1):
    """Return nth number of a sequence with the first two digits x and y.
    Defaults to fibonacci sequence otherwise."""
    if n <= 0:
        return 0
    l = [x, y]
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[n-1]
