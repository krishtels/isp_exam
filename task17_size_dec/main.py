def cached(size):
    def decorator(func):
        func.cached = {}

        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key not in func.cached:
                if len(func.cached) >= size:
                    print("clearing")
                    func.cached.clear()
                print("first time", key)
                func.cached[key] = func(*args, **kwargs)
            return func.cached[key]

        return wrapper
    return decorator


@cached(2)
def sum(a, b):
    return a + b