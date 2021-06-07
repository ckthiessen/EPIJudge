from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    

    # [1, 2, 3, 4]
    # Have to watch out for 9s
    # Esp if all elements are 9s
    # [9,9,9]
    # [9, 9, 9, 9]
    # [1, 0, 0, 0, 0]
    # [2, 0, 0, 0]
    # [1, 0, 0, 0]
    for i in range(len(A)-1, -1, -1):
        A[i] = (A[i] + 1) % 10
        if i == 0 and A[0] == 0:
            A[0] = 1
            A.append(0)
        if A[i] != 0:
            break

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
