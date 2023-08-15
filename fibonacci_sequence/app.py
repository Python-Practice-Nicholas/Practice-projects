

def fibonacci_sequence(num):
    ptr = 1
    sequence = [0, 1]

    while (ptr != num) and (ptr < num):

        next_val = ptr + sequence[-2]
        sequence.append(next_val)
        ptr = next_val

    return sequence
