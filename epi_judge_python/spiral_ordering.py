from typing import List

from test_framework import generic_test

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    L, R = 0, len(square_matrix)
    T, B = 0, len(square_matrix)

    res = []
    direction = 0
    while (L <= R and T <= B):
        if direction == 0:
            for i in range(L, R):
                res.append(square_matrix[T][i])
            T += 1
        elif direction == 1:
            for i in range(T, B):
                res.append(square_matrix[i][R - 1])
            R -= 1
        elif direction == 2:
            for i in range(R- 1, L - 1, -1):
                res.append(square_matrix[B - 1][i])
            B -= 1
        elif direction == 3:
            for i in range(B - 1, T - 1, -1):
                res.append(square_matrix[i][L])
            L += 1
        direction = (direction + 1) % 4

    return res

# def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
#     res = []
#     def process_layer(offset):
#         if offset == len(square_matrix) - offset - 1:
#             res.append(square_matrix[offset][offset])
#             return

#         res.extend(square_matrix[offset][-1 - offset])
#         res.extend(list(zip(*square_matrix)))[-1 - offset][offset:-1 - offset]
#         res.extend(square_matrix[-1 - offset][-1 - offset: offset: -1])
#         res.extend(list(zip(*square_matrix)))[-1 - offset][offset:-1 - offset]

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
