# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        begin = ListNode()
        begin.val = None
        begin.next = None
        current = begin
        while l1 and l2:
           if l1.val < l2.val:
               current.next = l1
               current = l1
               l1 = l1.next
           else:
               current.next = l2
               current = l2
               l2 = l2.next
        if l1:
            current.next = l1
        else:
            current.next = l2

        begin = begin.next
        return begin
