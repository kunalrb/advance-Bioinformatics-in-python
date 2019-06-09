import bisect
import time

def delta_y(y, x):

    delta = []
    for el in x:
        diff = abs(y - el)
        bisect.insort(delta, diff)
    return delta


def sublist(lst1, lst2):

    return set(lst1) <= set(lst2)


def place(list_l, x, width):

    list_l = sorted(list_l)
    if len(list_l) == 0:
        print("X = ",x)
        return
    y = list_l[-1]
    y_delta = delta_y(y, x)
    if sublist(y_delta, list_l):
        bisect.insort(x, y)
        for el in y_delta:
            list_l.remove(el)
        place(list_l, x, width)
        x.remove(y)
        for el in y_delta:
            bisect.insort(list_l, el)
    wy = width - y
    wy_delta = delta_y(wy, x)
    if sublist(wy_delta, list_l):
        bisect.insort(x, wy)
        for el in wy_delta:
            list_l.remove(el)
        place(list_l, x, width)
        x.remove(wy)
        for el in wy_delta:
            bisect.insort(list_l, el)
    return


def partial_digest(list_l):

    list_l = sorted(list_l)
    width = list_l[-1]
    list_l.remove(width)
    x = [0, width]
    place(list_l, x, width)
    return
tic = time.perf_counter()
partial_digest([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15])
toc = time.perf_counter()
print ("Runtime for partial Digest is ",toc-tic)
