# Source: http://rosettacode.org/
import doctest


def bubble_sort(seq):
    """
    Put your doctests here:

    >>> bubble_sort([])
    []

    >>> bubble_sort([2,7,3,5])
    [2, 3, 5, 7]

    >>> bubble_sort([3.5,6,2.2,7.8])
    [2.2, 3.5, 6, 7.8]

    >>> bubble_sort(['hello world'])
    ' dehllloorw'

    """
    changed = True
    while changed:
        changed = False
        if len(seq) !=0 and isinstance(seq[0], str):
            temp_seq = []
            for i in range(len(seq)):
                for j in range(len(seq[i])):
                    temp_seq.append(seq[i][j])
            for i in range(len(temp_seq)):
                for j in range(len(temp_seq) - i - 1):
                    if temp_seq[j] > temp_seq[j + 1]:
                        temp_seq[j], temp_seq[j + 1] = temp_seq[j + 1], temp_seq[j]
            new_seq = ''.join(temp_seq)
        else:
            new_seq = seq
            for i in range(len(seq) - 1):
                if seq[i] > seq[i + 1]:
                    new_seq[i], new_seq[i + 1] = seq[i + 1], seq[i]
                    changed = True
    return new_seq

print(bubble_sort(['hello world']))
doctest.testmod(verbose=True)