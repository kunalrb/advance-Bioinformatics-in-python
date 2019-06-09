def hamming_distance(string1, string2): 
    distance = 0

    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

if __name__ == '__main__':

    dna = input("Enter string 1: ")
    pattern = input("Enter string 2: ")

    print(str(hamming_distance(dna, pattern)))


