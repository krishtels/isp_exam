def logger(file, *args):
    def decorator(f):
        exceptions_to_log = []
        for exep in args:
            if type(exep) == type(Exception):
                exceptions_to_log.append(exep)

        def wrapper(*func_args, **func_kwargs):
            for ex in exceptions_to_log:
                try:
                    f(*func_args, **func_kwargs)
                    break
                except ex:
                    with open(file, 'w') as file_to_log:
                        file_to_log.write(str(exep)+f.__name__)
                except:
                    continue

        return wrapper
    return decorator


@logger('logger.txt', AssertionError, IndexError)
def f():
    a = [1,2]
    print(a[5])

f()