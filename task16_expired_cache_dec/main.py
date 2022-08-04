import time


def expired_cache(timeout):
    def decorator(func):
        func.cached = {}

        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key not in func.cached or time.time() - func.cached[key][1] > timeout:
                print("first time", key)
                func.cached[key] = func(*args, **kwargs), time.time()
            return func.cached[key][0]

        return wrapper
    return decorator


@expired_cache(1)
def sum(a, b):
    return a + b


sum(1, 2)
sum(2, 3)
time.sleep(0.5)
print("go")
sum(1, 2)
