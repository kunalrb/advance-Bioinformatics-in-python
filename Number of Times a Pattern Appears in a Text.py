# Compute the Number of Times a Pattern Appears in a Text

def patternCount(dna, pattern):

    patternsFound = 0

    for i in range(len(dna)):
        if dna[i:i + len(pattern)] == pattern:
            patternsFound += 1

    return patternsFound


if __name__ == '__main__':

    d na = input("Enter DNA sequence: ")
    pattern = input("Enter DNA pattern to count: ")

    print(str(patternCount(dna, pattern)))
