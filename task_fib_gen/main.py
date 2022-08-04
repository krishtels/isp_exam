def fib_gen(n):
    f1 = 1
    f0 = 0
    for i in range(n):
        yield f1 + f0
        f0_prev = f0
        f0 = f1
        f1 = f0_prev + f1


f = fib_gen(5)
for e in f:
    print(e)