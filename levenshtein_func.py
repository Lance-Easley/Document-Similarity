import doctest

def leven_distance(iterable1: str or list, iterable2: str or list) -> int:
    """Takes two strings or lists and will find the Levenshtein distance 
    between the two.

    Both iterables must be same type (str or list) for proper functionality.

    If given strings, function will find distance per character. If given 
    lists, function will find distance per term in list.

    Capitalization will be counted as a difference.

    >>> leven_distance('cat', 'hat')
    1
    >>> leven_distance('abcdef', 'azc3uf')
    3
    >>> leven_distance(['hi', 'there', 'kevin'], ['hello', 'there', 'kevin'])
    1
    """
    iterable1_count = len(iterable1) + 1
    iterable2_count = len(iterable2) + 1
    mem = []

    # Set memoize list length
    for i in range(0, iterable1_count):
        mem.append([])
        for j in range(0, iterable2_count):
            mem[i].append(None)

    # Assign empty string numbers to memoize chart
    #   Row
    for r in range(0, iterable1_count):
        mem[r][0] = r
    #   Column
    for c in range(0, iterable2_count):
        mem[0][c] = c

    # Fill in rest of chart
    for r in range(iterable1_count - 1):
        for c in range(iterable2_count - 1):
            if iterable1[r] == iterable2[c]:
                mem[r + 1][c + 1] = mem[r][c]
            else:
                mem[r + 1][c + 1] = min(
                    mem[r][c] + 1,
                    mem[r + 1][c] + 1,
                    mem[r][c + 1] + 1
                )
    # Get last number in chart
    return mem[-1][-1]

if __name__ == "__main__":
    print(doctest.testmod())