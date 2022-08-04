class Range:
    def __init__(self, start=0, end = None, step = 1):
        if step > 0:
            self.cur = start
            self.start = start
            self.end = end
            self.step = step
        else:
            raise IndexError

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.cur

        if self.cur != self.end:
            self.cur += self.step
        else:
            raise StopIteration
        return tmp

r = Range(-1,end=6,step=2)
for i in r:
    print(i)