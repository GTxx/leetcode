# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = head
        next = head.next if head else None
        if head:
            head.next = None
        while prev and next:
            prev1, next1 = next, next.next
            next.next = prev
            prev, next = prev1, next1
        return prev
