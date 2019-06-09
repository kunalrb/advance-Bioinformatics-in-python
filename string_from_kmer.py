import sys


def order_list(kmer_list, ordered_list=[], increment=0):
  
    if len(kmer_list) == 0:
        return ordered_list
    if increment == 0:
        ordered_list.append(kmer_list[0])
        foo = kmer_list[0]
        kmer_list.remove(foo)
    for el in kmer_list:
        if ordered_list[-1][1:] == el[:-1]:
            ordered_list.append(el)
            kmer_list.remove(el)
            order_list(kmer_list, ordered_list, 1)
        if ordered_list[0][:-1] == el[1:]:
            ordered_list.insert(0, el)
            kmer_list.remove(el)
            order_list(kmer_list, ordered_list, 1)
    return ordered_list


def string_from_kmer(kmer_list):

    kmer_list = order_list(kmer_list)
    dna_str = kmer_list[0]
    for index in range(1, len(kmer_list)):
        dna_str += kmer_list[index][-1]
    return dna_str


def load(path):

    with open(path) as input_data:
        kmer_list = [line.strip() for line in input_data]
        kmer_list = kmer_list[1:]
    return kmer_list


sys.setrecursionlimit(5000)
k = load('rosalind_ba3h.txt')
dna = string_from_kmer(k)
print(dna)
