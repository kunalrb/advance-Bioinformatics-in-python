
####Implement MotifEnumeration


from itertools import product
import numpy as np



def hamming_distance(string1, string2):
    distance = 0

    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def MotifEnumeration(Dna, k, d):
    # Compute all of the possible kmers
    possible_k_mers = [''.join(x) for x in product(['A','T','C','G'], repeat= k)]
    for each_sequence in Dna:
        # Generate the kmers
        kmers_dna = []
        for i in range(len(each_sequence)+1 - k):
            kmers_dna.append(each_sequence[i:i+k])
        # Filter the kmers for the ones with the desired Hamming distance
        possible_k_mers = [x for x in possible_k_mers for y in kmers_dna if hamming_distance(string1=x, string2=y) <= d]

    return(list(set(possible_k_mers)))


######### Enter the input file here,make sure you code file n dataset fie is in same directory
file = open('rosalind_ba2a.txt', 'r')
input_data = file.readlines()
file.close()
input_data = [x.split('\n') for x in input_data]
######## You need to put the indexes right in here for the file  for the test(input start row number to end number)
set_of_sequences = input_data[1:11]
set_of_sequences = [x[0] for x in set_of_sequences]


if __name__ == '__main__':
    patternSize = int(input("Enter DNA pattern size: "))
    mismatch = int(input("Enter number of mismatch: "))


    for pattern in MotifEnumeration(set_of_sequences, patternSize,mismatch):
        print(pattern + " ", end="")





