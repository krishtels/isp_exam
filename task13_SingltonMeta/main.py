class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    # Клиентский код.

    a = MyClass()
    b = MyClass()

    if id(a) == id(b):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")