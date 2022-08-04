class StringField:
    def __init__(self):
        self.__type = str
        self.__value = str()
        self.name = None

    def __get__(self, instance, owner):
        return getattr(instance, self.name, str())

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ModelCreator(type):
    def __new__(cls, name, bases, namespace):
        storage = set()

        for base in bases:
            if hasattr(base, '__slots__'):
                storage.update(base.__slots__)

        for k, v in namespace.items():
            if isinstance(v, StringField):
                v.name = f"_{k}"
                storage.add(v.name)

        def __new__(cls, *args, **kwargs):
            instance = object.__new__(cls)
            for k, v in kwargs.items():
                if f'_{k}' in cls.__slots__:
                    setattr(instance, k, v)
            return instance

        namespace['__new__'] = __new__
        namespace['__slots__'] = list(storage)

        new_cls = super().__new__(cls, name, bases, namespace)
        return new_cls


class Student(metaclass=ModelCreator):
    name = StringField()
    address = StringField()


s = Student(name='abacaba')
print(s.name)
