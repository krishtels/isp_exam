def QuickSort(A, l, r):
    if l >= r:
        return
    else:
        # q = random.choice(A[l:r + 1])
        q = A[(l+r)//2]
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
                QuickSort(A, l, j)
                QuickSort(A, i, r)

# Проверяем, что оно работает
random_list_of_nums = [22, 5, 1, 18, 99]
print(QuickSort(random_list_of_nums, 0, len(random_list_of_nums)-1))
print(random_list_of_nums)