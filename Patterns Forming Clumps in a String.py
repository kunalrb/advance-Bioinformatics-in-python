# Find Patterns Forming Clumps in a String

def clumps(dna, frameSize, clumpSize, requiredOccurence):

    dnaClumpsWithRequiredOccurence = set()

    for i in range(len(dna)):
        # Process next frame
        if i + frameSize <= len(dna):
            subDna = dna[i:i + frameSize]

            # Within the frame find clumps of given size and count its frequencies
            dnaClumps = dict()

            for j in range(len(subDna)):
                if j + clumpSize <= len(subDna):
                    dnaClump = subDna[j:j + clumpSize]

                    if dnaClump in dnaClumps.keys():
                        dnaClumps[dnaClump] += 1
                    else:
                        dnaClumps[dnaClump] = 1

            # For each dna clump, filter only those that meet the required occurence
            for dnaClump, frequency in dnaClumps.items():
                if frequency >= requiredOccurence:
                    dnaClumpsWithRequiredOccurence.add(dnaClump)

    return dnaClumpsWithRequiredOccurence


if __name__ == '__main__':
    dna = input("Enter DNA sequence: ")
    frameSize = int(input("Input frame size (L): "))
    clumpSize = int(input("Input the size of a DNA pattern to count: "))
    requiredOccurence = int(input("Input the required occurence that is required for a DNA pattern to be considered a clump: "))

    for clump in clumps(dna, frameSize, clumpSize, requiredOccurence):
        print(clump + " ", end="")
