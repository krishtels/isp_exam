def permutations(k, n):
    numbers = list(range(n))
    yield numbers[:k] # first perm

    while True:
        for j in range(k, n):
            if numbers[j] > numbers[k-1]:
                break
        else:
            j = n

        if j < n:
            numbers[k-1], numbers[j] = numbers[j], numbers[k-1] # swap
            yield numbers[:k]
        else:
            numbers[k:] = reversed(numbers[k:])  # reverse elements from position i+1 till the end of the sequence

            for i in range(k-2, -1, -1):
                if numbers[i] < numbers[i+1]:
                    break
            else:
                return

            for j in range(n-1, i, -1):
                if numbers[j] > numbers[i]:
                    break

            numbers[i], numbers[j] = numbers[j], numbers[i]
            numbers[i+1:] = reversed(numbers[i+1:])  # reverse elements from position i+1 till the end of the sequence
            yield numbers[:k]


for perm in permutations(3, 5):
    print(perm)


