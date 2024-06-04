#!/usr/bin/env python

import numpy as np

MIN_LENGTH = 2
file = open("poem.txt", "r")
text = file.read()
file.close()

text = list(text)
count = len(text)
m = np.zeros((count, count))

# Calculate the co-occurrence matrix on the text against itself
# e.g. the columns represent the chars in the text and the rows
# represent the chars in the text
for i in range(count):
    for j in range(count):
        if text[i].lower() == text[j].lower():
            m[i][j] = 1


def get_indices(length, row = 0, col = 1):
    """
    :param length: length of text (eg - number of rows)
    :param row: row at which to start calculating diagonal indices
    :param col: col at which to start calculating diagonal indices
    :return: array of tuples (indices)
    """
    indices = []
    while row < length and col < length:
        indices.append((row, col))
        row += 1
        col += 1
    return indices


def get_diag(m, row = 0, col = 1):
    """
    :param m: co-occurrence matrix
    :param row: row at which to start
    :param col: col at which to start
    :return: substrings found by sequences of 1s on a diagonal
    """
    assert col > row
    indices = get_indices(count, row, col)
    substrings = []
    curr = ''
    for ind in indices:
        # if the characters match
        if m[ind[0]][ind[1]] == 1:
            char = text[ind[0]]
            curr += char

        # if we are either at the end of the row or the end of a substring
        if len(curr) != 0 and (m[ind[0]][ind[1]] != 1 or ind[1] == count-1):
            if len(curr) >= MIN_LENGTH:
                substrings.append(curr)
            curr = ''
    return substrings


def main():
    longest = ''
    for i in range(1, count):
        s = get_diag(m, 0, i)
        for sub in s:
            if len(sub) > len(longest):
                longest = sub
    print(longest)

if __name__ == '__main__':
    main()

