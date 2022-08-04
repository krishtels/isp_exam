from typing import Any, Iterable
from copy import deepcopy as dc


class CollectionFormater:
    def __init__(self, collection: Iterable):
        self.iterable = collection

    def __iter__(self):
        return self.iterable.__iter__()

    def select(self, func: bool(Any)):
        new_col = dc(CollectionFormater(self.iterable))
        for i in range(len(self.iterable)):
            if not func(self.iterable[i]):
                del new_col.iterable[i]
        return new_col


a = CollectionFormater([1, -2, 4, 3, 6, 5])
b = a.select(lambda x: x > 0)
for i in b:
    print(i)

# for i in a:
#     print(i)