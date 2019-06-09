import numpy as np


def read_data(path):

    with open(path) as input_data:
        temp = [line.strip() for line in input_data]
    first_str = temp[0]
    second_str = temp[1]
    return first_str, second_str


def edit_distance(v, w):

    t = np.zeros((len(v), len(w)))
    for index0 in range(t.shape[0]):
        t[index0][0] = index0
    for index1 in range(t.shape[1]):
        t[0][index1] = index1
    for index2 in range(1, len(v)):
        for index3 in range(1, len(w)):
            if v[index2-1] == w[index3-1]:
                t[index2][index3] = t[index2-1][index3-1]
            else:
                t[index2][index3] = min(t[index2-1][index3], t[index2-1][index3-1], t[index2][index3-1]) + 1
    return t


string1, string2 = read_data('rosalind_ba5g-2.txt')
dis_test = edit_distance(string1, string2)
print('The edit distance between the two strings is equal to ' + str(int(dis_test[-1][-1])))
