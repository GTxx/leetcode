# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt_head = ListNode(None)
        lt_current = lt_head
        gte_head = ListNode(None)
        gte_current = gte_head
        current = head
        while current:
            if current.val < x:
                lt_current.next = current
                lt_current = current
                current = current.next
            else:
                gte_current.next = current
                gte_current = current
                current = current.next

        lt_current.next = None
        gte_current.next = None
        lt_current = lt_head
        while lt_current.next:
            lt_current = lt_current.next
        lt_current.next = gte_head.next
        return lt_head.next
