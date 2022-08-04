class MetaControl(type):
    _counter = {}

    def __new__(cls, name, bases, attrs):
        cls._counter[name]=0
        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        cls._counter[cls.__name__] += 1
        return super.__call__(*args, **kwargs)


class MyClass(metaclass=MetaControl):
    pass


if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    print(MyClass._counter)