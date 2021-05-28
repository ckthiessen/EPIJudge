from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string


def int_to_string(x: int) -> str:
    itos = []

    neg = False
    if(x < 0):
        neg = True
        x = abs(x)

    while True:
        next_int = x % 10
        itos.append(chr(ord('0') + next_int))
        x = x // 10
        if x == 0:
            break

    return ('-' if neg else '') + ''.join(reversed(itos))



def string_to_int(s: str) -> int:
    neg = False
    start = 0

    if(s[0] == '-'):
        neg = True
        start = 1
    
    if(s[0] == '+'):
        start = 1

    res = 0
    for i in range(start, len(s)):
        res += ord(s[i]) - ord('0')
        res *= 10 if i < len(s) - 1 else 1

    return (-res if neg else res)

# def string_to_int(s: str) -> int:
#     return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    # print(string_to_int('4176473'))
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
