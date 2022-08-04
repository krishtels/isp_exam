import threading
import time


arrays = [
    [1, 5, 3, 8, 3],
    [1, 1, 8, 9, 9, 4, 4, 7, 5],
    [1, 2, 9, 8, 7, 6],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [5, 4],
]


def sorting(lst):
    time.sleep(1)
    if len(lst) > 2:
        lst1 = sorting(lst[:len(lst) // 2])
        lst2 = sorting(lst[len(lst) // 2:])

        lst.clear()

        while lst1 and lst2:
            if lst1[0] <= lst2[0]:
                lst.append(lst1[0])
                lst1 = lst1[1:]
            else:
                lst.append(lst2[0])
                lst2 = lst2[1:]

        if lst1:
            lst.extend(lst1)
        if lst2:
            lst.extend(lst2)

        return lst

    elif len(lst) == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    else:
        return lst


def main():
    threads = []
    for arr in arrays:
        x = threading.Thread(target=sorting, args=(arr,))
        x.start()
        threads.append(x)

    for thr in threads:
        thr.join()

    for arr in arrays:
        print(arr)


if __name__ == '__main__':
    main()
