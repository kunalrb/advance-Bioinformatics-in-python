####generate K-mer compositiion

def k_mer_comp(k, seq):
    comp_list = []
    while len(seq) >= k:
        comp = seq[0:k]
        seq = seq[1:]
        comp_list.append(comp)
    return comp_list


# test
def load(path):
    with open(path) as input_data:
        foo = input_data.readline().split('\n')
        k = int(foo[0])
        bar = [line.strip() for line in input_data]
        dna_string = bar[0]
    return k, dna_string


k1, dna = load('rosalind_ba3a.txt')
compositions = k_mer_comp(k1, dna)
for composition in compositions:
    print(composition)





