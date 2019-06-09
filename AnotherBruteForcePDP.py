from DeltaX_from_X import multiset_from_X
from itertools import combinations
import math
import  time


def another_brute_force(list_l, n, all_x=False):

    list_l = sorted(list_l)
    m = list_l[-1]
    x = [0, m]
    new_list_l = set(list_l[:-1])
    combs = list(combinations(new_list_l, n-2))
    no_sol = True
    x_list = []
    for comb in combs:
        x = sorted(x + list(comb))
        delta_x = multiset_from_X(x)
        if delta_x == list_l:
            no_sol = False
            if not all_x:
                return x
            x_list.append(x)
        x = [0, m]
    if no_sol:
        print('No solution')
    else:
        return x_list


def another_brute_force2(list_l, all_x=False):

    length = len(list_l)
    delta = 1 + 8 * length
    n = int((1 + math.sqrt(delta))/2)
    x_or_x_list = another_brute_force(list_l, n, all_x)
    return x_or_x_list


tic = time.perf_counter()
L = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
brute_3 = another_brute_force2(L , True)
print("List of all X such that ΔX=L ----> ",brute_3)
toc = time.perf_counter()
print ("Runtime for AnotherBruteForcePDP is ",toc-tic)
