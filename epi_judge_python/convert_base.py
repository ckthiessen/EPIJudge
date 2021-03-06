from test_framework import generic_test
import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def create_new_base(num, base):
        return ('' if num == 0 else create_new_base(num // base, base) + string.hexdigits[num % base].upper())



    is_negative = num_as_string[0] == '-'
    nai = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if nai == 0 else create_new_base(nai, b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
