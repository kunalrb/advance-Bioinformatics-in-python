####Find a Profile-most Probable k-mer in a String


import numpy as np

def ProfileMostProbable(string, k, matrix_p):
    dict_indexes = dict({'A' : [0],
                         'C' : [1], 
                         'G' : [2], 
                         'T' : [3]})
    
    # Generate the kmers
    kmers = []
    for i in range(len(string)+1 - k):
        kmers.append(string[i:i+k])
    max_probability = 0
    try:
        for each_kmer in kmers: 
            each_kmer_prob = [] 
            for (each_nucleotide, probabilities) in zip(each_kmer, matrix_p): 
                index = dict_indexes[each_nucleotide][0]
                each_kmer_prob.append(probabilities[index])
            probability_kmer = np.array(each_kmer_prob).prod()
            if probability_kmer > max_probability: 
                max_probability = probability_kmer
                resulting_kmer = each_kmer
        return(resulting_kmer)
    except:
        resulting_kmer = kmers[0]
        return(resulting_kmer)

#######insert files name for input data(code and data file should be in same directory)
file = open('rosalind_ba2c.txt', 'r')
input_data = file.readlines()
file.close()
input_data = [x.split('\n') for x in input_data]

### Fill in the index for the input sequence(row number from input)
sequence_in = input_data[0][0]

### Fill in the indexes for the matrix
matrix_prob = np.array([[float(x) for x in input_data[2][0].split(' ')],
                       [float(x) for x in input_data[3][0].split(' ')],
                       [float(x) for x in input_data[4][0].split(' ')],
                       [float(x) for x in input_data[5][0].split(' ')]])

matrix_prob = matrix_prob.T
### Fill here with the k-mer
k = 6

Sequence = ProfileMostProbable(string = sequence_in, k = k, matrix_p= matrix_prob)

print(Sequence)
