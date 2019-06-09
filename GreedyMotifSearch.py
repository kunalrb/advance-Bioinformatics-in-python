#########Implement GreedyMotifSearch

import numpy as np


def hamming_distance(string1, string2): 
    distance = 0

    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def CreateProfile(string, k, alignment = False): 
    ''' Creates a probability profile matrix from a string'''
    if alignment:
        kmers = string
    else:
        # Create k-mers
        kmers = []
        for i in range(len(string)+1 - k):
            kmers.append(string[i:i+k])
        # Initialize an empty profile
    profile = []
    #amount of kmers
    kmers_count = len(kmers)
#    for each position of the given kmer 
    for each_position in range(k): 
        A = [x[each_position] for x in kmers].count('A') / kmers_count
        C = [x[each_position] for x in kmers].count('C') / kmers_count
        G = [x[each_position] for x in kmers].count('G') / kmers_count
        T = [x[each_position] for x in kmers].count('T') / kmers_count
        profile.append([A,C,G,T])
    return(np.array(profile))

def Consensus(Dna):
    consensus_sequence = []  
    nucleotides = ['A', 'C', 'G', 'T']
#    for each_sequence in Dna: 
    for i in range(len(Dna[0])): 
        i_nucleotide = [x[i] for x in Dna]
        count = 0 
        for each_nucleotide in nucleotides: 
            count_n = i_nucleotide.count(each_nucleotide)
            if count_n > count: 
                count = count_n
                consensus_nucleotide = each_nucleotide
        consensus_sequence.append(consensus_nucleotide)
    return(''.join(consensus_sequence))
#            

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
#
#
def GreedyMotifSearch(Dna, k, t):
  best_motifs = []
  consensos = []
  kmers_first_seq = []
  for i in range(len(Dna[0])+1 - k):
        kmers_first_seq.append(Dna[0][i:i+k])
  
  kmers_qty = len(kmers_first_seq)
  score_motifs = []
  for i in range(kmers_qty):
      motif_orig = []
      motif_orig.append(kmers_first_seq[i])
      for n in range(1,t):
          profile = CreateProfile(string = motif_orig, k= k, alignment = True)
          kmer_2 = ProfileMostProbable(string= Dna[n], k=k, matrix_p = profile)
          motif_orig.append(kmer_2)
      best_motifs.append(motif_orig)
      consensus_motif = Consensus(motif_orig)
      score_motifs.append(sum([hamming_distance(string1= x, string2= consensus_motif) for x in motif_orig]))

  index_lower_score = score_motifs.index(min(score_motifs))
  result = best_motifs[index_lower_score]
  return(result)

#######insert files name for input data(code and data file should be in same directory)
file = open('rosalind_ba2d.txt', 'r')
input_data = file.readlines()
file.close()
input_data = [x.split('\n') for x in input_data]

#####insert the index for start and end row number for input sequence
sequence_in = input_data[1:26]
sequence_in = [x[0] for x in sequence_in]
k = 12
t = 25

Sequences = GreedyMotifSearch(Dna= sequence_in, k= k , t= t)
Sequences.sort()
print(Sequences)
