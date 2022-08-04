import inspect


class MetaClass(type):
    def __init__(cls, name, parents, attr):
        with open("data.json", "r") as f:
            data = eval(f.read())
        for k, v in data.items():
            setattr(cls, k, v)

        super().__init__(name, parents, attr)


class A(metaclass=MetaClass):
    pass


a = A()
print(inspect.getmembers(A))
print(a.age)