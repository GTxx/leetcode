# Definition for singly-linked list.
from typing import List


def cons(lst):
    head = ListNode()
    current = head
    for i in lst:
        n = ListNode(i)
        current.next = n
        current = n
    return head.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        idx = 0
        res = {}
        while head:
            while stack and stack[-1][1] < head.val:
                idx1, value = stack.pop()
                res[idx1] = head.val
            stack.append((idx, head.val))
            idx += 1
            head = head.next
        res1 = [0 for _ in range(idx)]
        for k, v in res.items():
            res1[k] = v
        return res1


if __name__ == "__main__":
    s = Solution()
    from algorithms import test

    l = cons([2, 1, 5])
    test(l, [5, 5, 0], s.nextLargerNodes)
    l1 = cons([2, 7, 4, 3, 5])
    test(l1, [7, 0, 5, 5, 0], s.nextLargerNodes)
