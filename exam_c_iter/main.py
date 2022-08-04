class Iterator:
    def __iter__(self):
        return self

    def __init__(self, n, k):
        self.count = 0
        self.n = n
        self.k = k
        self.numbers = tuple(range(n))
        self.indexes = list(range(k))

    def __next__(self):
        next_perm = self.next(self.numbers, self.indexes, self.n, self.k, self.count)
        self.count += 1
        if next_perm:
            return tuple(next_perm)
        else:
            raise StopIteration

    @staticmethod
    def next(numbers, indexes, n, r, count):
        if count == 0:
            return tuple(numbers[i] for i in indexes)
        count += 1
        while True:
            for i in reversed(range(r)):
                if indexes[i] < i + n - r:
                    break
            else:
                return
            indexes[i] += 1
            for j in range(i + 1, r):
                indexes[j] = indexes[j - 1] + 1
            return tuple(numbers[i] for i in indexes)


for i in Iterator(5, 2):
    print(i)


