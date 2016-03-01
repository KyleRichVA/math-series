

def fibonacci(n):
    if n <= 0:
        return 0
    l = [0, 1]
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[n-1]


def lucas(n):
    pass
