import bisect

def multiset_from_X(set_int):

    n = len(set_int)
    multiset = []
    for index0 in range(n):
        for index1 in range(index0 + 1, n):
            diff = (set_int[index0] - set_int[index1]) * -1
            bisect.insort(multiset, diff)
    return multiset


x = [0, 6, 9, 10, 11, 12, 15]
delta_X = multiset_from_X(x)
# print("If X =",x,"so ΔX = ",delta_X)

