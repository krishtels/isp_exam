def parametrise_decorator(*args, **kwargs):
    def pure_decorator(f):
        def wrapped(*func_args, **func_kwargs):
            print(f'Dec parametr:{args}, {kwargs}')
            print(f'Func parametr:{func_args}, {func_kwargs}')
            f()
        return wrapped
    return pure_decorator


@parametrise_decorator(3, age=22)
def foo():
    print('hello')


foo(4, (1,2), f=2)