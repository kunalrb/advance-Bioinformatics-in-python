import numpy as np


def compare(seq_1, seq_2, match, mismatch):

    assert len(seq_1) == len(seq_2) == 1
    if seq_1 == seq_2:
        return match
    else:
        return mismatch


def fill_arrow_matrix(index):

    arrow_string = ''
    if index == 0:
        arrow_string = 'D'
    elif index == 1:
        arrow_string = 'S'
    elif index == 2:
        arrow_string = 'T'
    return arrow_string


def traceback(seq_1, seq_2, arrow_matrix, start_pos, str_1='', str_2=''):

    if start_pos[0] != -1 and start_pos[1] != -1:
        str_1 = ''
        str_2 = ''
        if arrow_matrix[start_pos[0]][start_pos[1]] == 'D':
            str_1 += seq_1[start_pos[0]]
            str_2 += seq_2[start_pos[1]]
            start_pos = [start_pos[0]-1, start_pos[1]-1]
        if arrow_matrix[start_pos[0]][start_pos[1]] == 'S':
            str_1 += seq_1[start_pos[0]]
            str_2 += '-'
            start_pos = [start_pos[0], start_pos[1]-1]
        if arrow_matrix[start_pos[0]][start_pos[1]] == 'T':
            seq_1 += '-'
            seq_2 += seq_2[start_pos[1]]
            start_pos = [start_pos[0]-1, start_pos[1]]
        temp_1, temp_2 = traceback(seq_1, seq_2, arrow_matrix, start_pos)
        str_1 += temp_1
        str_2 += temp_2
    return str_1, str_2


def local_alignment(seq_1, seq_2, match, mismatch, indel):

    score_matrix = np.zeros((len(seq_1) + 1, len(seq_2) + 1))
    arrow_matrix = np.zeros((len(seq_1), len(seq_2)), dtype=str)
    score = 0
    loc_opt = (0, 0)
    for i in range(1, len(seq_1) + 1):
        for j in range(1, len(seq_2) + 1):
            temp_list = [score_matrix[i - 1][j - 1] + compare(seq_1[i - 1], seq_2[j - 1], match, mismatch),
                         score_matrix[i][j - 1] + indel, score_matrix[i - 1][j] + indel]
            score_matrix[i][j] = max(temp_list)
            index = np.argmax(temp_list)
            arrow_matrix[i-1][j-1] = fill_arrow_matrix(index)
            if score_matrix[i][j] >= score:
                score = score_matrix[i][j]
                loc_opt = [i, j]
    modified_loc_opt = [loc_opt[0]-1, loc_opt[1]-1]
    str_1, str_2 = traceback(seq_1, seq_2, arrow_matrix, modified_loc_opt)
    list_str_1 = [c for c in str_1]
    list_str_2 = [c for c in str_2]
    list_str_1.reverse()
    list_str_2.reverse()
    return score, loc_opt, score_matrix, arrow_matrix, list_str_1, list_str_2


s1, opt1, A1, arrow1, str_11, str_12 = local_alignment('1213434222', '1343422421', 1, -1, -0.5)

# print("Score matrix")
# print(A1)
print("Optimal Score = " + str(s1) + " at position " + str(opt1) + " in Score matrix")
# print("Arrow matrix")
# print(arrow1)
print("Optimal local alignment:")
print(", ".join([str(x) for x in str_11]))
print(", ".join([str(x) for x in str_12]))
