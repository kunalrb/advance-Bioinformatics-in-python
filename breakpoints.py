def read_data(path):

    with open(path) as input_data:
        temp = [line.strip() for line in input_data]
    s = temp[1].replace('(', '').replace(')', '')
    integer_list = s.split()
    integer_list = [int(c) for c in integer_list]
    return integer_list


def calculate_breakpoints(seq):

    n = len(seq)
    new_seq = seq[:]
    new_seq.insert(0, 0)
    new_seq.extend([n+1])
    num_breakpoints = 0
    for index in range(len(new_seq)-1):
        distance = new_seq[index+1] - new_seq[index]
        if distance != 1:
            num_breakpoints += 1
    return num_breakpoints

sequence = read_data('rosalind_ba6b.txt')
breakpoints = calculate_breakpoints(sequence)
print('The number of breakpoints in the sequence is: ' + str(breakpoints))
