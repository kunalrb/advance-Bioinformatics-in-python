# Find the Complement of a String and reverse the compliment

def complement(dna):

    dnaComplement = ""

    # Replace each letter to their appropriate complement
    for letter in reversed(dna):
        if letter == "A":
            dnaComplement += "T"
        elif letter == "C":
            dnaComplement += "G"
        elif letter == "T":
            dnaComplement += "A"
        elif letter == "G":
            dnaComplement += "C"

    return dnaComplement


if __name__ == '__main__':
    dna = input("Enter DNA sequence: ")
    print(complement(dna))
