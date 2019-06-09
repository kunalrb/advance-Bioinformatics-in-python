
#Most Frequent Words with Mismatches in a String


def hamming_distance(string1, string2):
    distance = 0

    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def CountDistance(string, pattern, d = 1):
    len_kmer = len(pattern)
    kmers = []
    for i in range(len(string)+1 - len_kmer):
        kmers.append(string[i:i+len_kmer])

    counter = 0
    for each_kmer in kmers:
        if (hamming_distance(each_kmer, pattern) <= d):
            counter += 1

    return(counter)


def FindVariants(string, mismatches = 1):
    def DistanceOne(string_in):
        sequences_out = []
        nucleotides = ['A', 'T', 'C', 'G']
        for i in range(len(string_in)):
            for each_nucleotide_m in nucleotides:
                sequence_in = list(string_in)
                sequence_in[i] = each_nucleotide_m
                sequence = ''.join(sequence_in)
                sequences_out.append(sequence)
        return(list(set(sequences_out)))

    if mismatches == 1:
        return(DistanceOne(string_in= string))

    elif mismatches > 1:
        sequences_out = []
        sequences_out_cp = DistanceOne(string_in= string)
        for i in range(mismatches-1):

            for each_sequence in sequences_out_cp:

                sequences_out.append(DistanceOne(string_in = each_sequence))
            sequences_out_cp = sequences_out.copy()
            sequences_out_cp = [x for y in sequences_out_cp for x in y]
        return(list(set([x for y in sequences_out for x in y])))

def FindMostFrequentPattern(string, k, d):
    max_occurrence = 0
    list_of_frequents_kmers = []

    possible_k_mers = []
    for i in range(len(string)+1 - k):
        possible_k_mers.append(string[i:i+k])

    kmers_list = []
    for each_possible_kmer in possible_k_mers:
        kmers_list.append(FindVariants(each_possible_kmer, mismatches = 2))
    kmers_list = [x for y in kmers_list for x in y]

    for each_kmer in kmers_list:
        counts = CountDistance(string = string, pattern= each_kmer, d = d)
        if counts > max_occurrence:
            list_of_frequents_kmers = []
            list_of_frequents_kmers.append(each_kmer)
            max_occurrence = counts
        elif counts == max_occurrence:
            list_of_frequents_kmers.append(each_kmer)
    return(list(set(list_of_frequents_kmers)))


if __name__ == '__main__':
    dna = input("Enter DNA sequence: ")
    patternSize = int(input("Enter DNA pattern size: "))
    mismatch = int(input("Enter number of mismatch: "))


    for pattern in FindMostFrequentPattern(dna, patternSize,mismatch):
        print(pattern + " ", end="")
