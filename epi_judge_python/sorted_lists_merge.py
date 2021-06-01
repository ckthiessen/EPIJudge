from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    
    # 2 iterators
    # both start at head
    # when one ends, make sure to fill rest of other list
    sentinel = res = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            res.next, L1 = L1, L1.next
        else:
            res.next, L2 = L2, L2.next
        res = res.next

    res.next = L1 or L2
    return sentinel.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
