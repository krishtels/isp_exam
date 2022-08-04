import types


class Logger:
    def __init__(self):
        self.log = []

    def __str__(self):
        return str(self.log)

    def logging(self, f):
        def wrapper(*args, **kwargs):
            res = [f.__name__, args, kwargs]
            s = f(*args, **kwargs)
            res.append(s)
            self.log.append(res)
            return s
        return wrapper

    def __getattribute__(self, item):
        if isinstance(super().__getattribute__(item), types.MethodType) and item != "logging":
            attr = self.logging(super().__getattribute__(item))

        else:
            attr = super().__getattribute__(item)
        return attr


class A(Logger):
    def met1(self, el):
        return "чего надо {}".format(el)

    x = 6


a = A()
print(a.x)
print(a.met1(9))
print(a.met1(10))
print(a.log)
