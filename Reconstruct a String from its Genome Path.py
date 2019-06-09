def reconstruct(genome_path_list):
    string = genome_path_list[0]
    for index in range(1, len(genome_path_list)):
        string += genome_path_list[index][-1:]
    return string


with open('rosalind_ba3b.txt') as input_data:
    path_list = [line.strip() for line in input_data]

seq = reconstruct(path_list)
print(seq)
