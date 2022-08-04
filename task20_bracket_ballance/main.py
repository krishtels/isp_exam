def is_balance(st, bstart='([{', bend=')]}'):
    dt = dict.fromkeys(range(len(bend)), 0)
    for s in st:
        if s in bstart:
            dt[bstart.index(s)] += 1
        elif s in bend:
            i = bend.index(s)
            dt[i] -= 1
            if dt[i] < 0:
                return False
    return not any(dt.values())


st = input('Input your str\n')
print(is_balance(st))
