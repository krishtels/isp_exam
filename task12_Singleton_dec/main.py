def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass

if __name__ == "__main__":
    # Клиентский код.

    a = MyClass()
    b = MyClass()

    if id(a) == id(b):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")