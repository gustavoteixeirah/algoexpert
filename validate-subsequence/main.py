def isValidSubsequence(array, sequence):
    seq_size = len(sequence)
    seen = seq_size
    for i, x in enumerate(array):
        if seen == 0:
            break
        if sequence[seq_size - seen] == x:
            seen = seen - 1
    return seen == 0
    pass


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
