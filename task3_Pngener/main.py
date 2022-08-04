def permutations(n):
    numbers = list(range(n))
    yield numbers  # first perm

    while True:
        for i in range(n-2, -1, -1):
            if numbers[i] < numbers[i+1]:
                break
        else:
            return

        for j in range(n-1, i, -1):
            if numbers[j] > numbers[i]:
                break

        numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i+1:] = reversed(numbers[i+1:])  # reverse elements from position i+1 till the end of the sequence
        yield numbers


for e in permutations(3):
    print(e)