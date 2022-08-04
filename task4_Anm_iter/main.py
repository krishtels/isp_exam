class PermutationIterator:
    def __iter__(self):
        return self

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.count = 0
        self.cur_numbers = list(range(n))

    def __next__(self):
        next_perm = next_permutation(self.cur_numbers, self.m, self.n, self.count)
        self.count += 1
        if next_perm:
            return next_perm
        else:
            raise StopIteration


def next_permutation(numbers, k, n, count):
    if count == 0:
        return numbers[:k]

    for j in range(k, n):
        if numbers[j] > numbers[k - 1]:
            break
    else:
        j = n

    if j < n:
        numbers[k - 1], numbers[j] = numbers[j], numbers[k - 1]  # swap
        return numbers[:k]
    else:
        numbers[k:] = reversed(numbers[k:])  # reverse elements from position i+1 till the end of the sequence

        for i in range(k - 2, -1, -1):
            if numbers[i] < numbers[i + 1]:
                break
        else:
            return

        for j in range(n - 1, i, -1):
            if numbers[j] > numbers[i]:
                break

        numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i + 1:] = reversed(numbers[i + 1:])  # reverse elements from position i+1 till the end of the sequence
        return numbers[:k]


for gg in PermutationIterator(3, 2):
    print(gg)