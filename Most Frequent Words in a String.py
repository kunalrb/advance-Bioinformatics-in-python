# Frequent words problem

def mostFrequentPatterns(dna, patternSize):

    # Find the patterns and their frequency
    patterns = dict()

    for i in range(len(dna)):
        if i + patternSize <= len(dna):
            pattern = dna[i:i + patternSize]

            if pattern in patterns.keys():
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1

    # Find the highest frequency
    highestFrequency = 0

    for frequency in patterns.values():
        if frequency > highestFrequency:
            highestFrequency = frequency

    # Find all patterns that has the highest frequency
    mostFrequentPatterns = list()

    for pattern in patterns.keys():
        if patterns[pattern] == highestFrequency:
            mostFrequentPatterns.append(pattern)

    return mostFrequentPatterns


if __name__ == '__main__':
    dna = input("Enter DNA sequence: ")
    patternSize = int(input("Enter DNA pattern size: "))


    for pattern in mostFrequentPatterns(dna, patternSize):
        print(pattern + " ", end="")
