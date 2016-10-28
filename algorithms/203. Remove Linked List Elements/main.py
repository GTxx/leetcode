# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_head.next = head
        current = new_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return new_head.next



