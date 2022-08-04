from functools import cmp_to_key


def cached(cmp):
    if type(cmp) != type(cached):
        raise ValueError("cmp should be a function!")

    def decorator(func):
        def wrapper(*args, **kwargs):
            args = tuple(sorted(args, key=cmp_to_key(cmp)))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cmp(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


@cached(cmp)
def sum(a, b, c):
    return a * 100 + b * 10 + c


print(sum(2, 1, 3))
print(sum(2, 4, 1))
print(sum(1, 9, 2))
print(sum(1, 6, 6))