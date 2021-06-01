from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    sentinel = sublist_head = ListNode(0, L)

    # start index at 1
    for _ in range(1, start):
        sublist_head = sublist_head.next

    #           ↑-------↓
    # S -> 1   2 ← 3    4 -> 5 -> 6 -> None
    #      ↓-------↑
    #      SH  SI   T

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    
    return sentinel.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
