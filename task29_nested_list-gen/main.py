def lazy_flat_list(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from lazy_flat_list(elem)
        else:
            yield elem

# lst = [[1, 1], [2], [1, 1]]
lst = [[1, [1, 3]], 2, [1, 4, [6]]]
for i in lazy_flat_list(lst):
    print(i, end=" ")