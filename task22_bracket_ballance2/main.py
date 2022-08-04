def check(st, *args):
    bstart = []
    bend = []
    for bracket_tuple in args:
        bstart.append(bracket_tuple[0])
        bend.append(bracket_tuple[1])

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


# print(check('([]', ('(', ')')))
# print(check('([)]', ('(', ')'))) #False
# print(check('({{}]})', ('{', '}'), ('(', ')'))) #True
# print(check('({{}]})', ('{', '}'), ('(', ')'), ('[', ']'))) #False

