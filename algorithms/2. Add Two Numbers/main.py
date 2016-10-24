# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_current = l1
        l2_current = l2
        head = ListNode(0)
        l = head
        while l1_current or l2_current:
            if l1_current:
                l1_val = l1_current.val
                l1_current = l1_current.next
            else:
                l1_val = 0

            if l2_current:
                l2_val = l2_current.val
                l2_current = l2_current.next
            else:
                l2_val = 0
            add = l.val + l1_val + l2_val
            l.val = add % 10
            over = add // 10
            if l1_current or l2_current or over >= 1:
                next = ListNode(over)
                l.next = next
                l = next

        return head

def list_2_node(lst):
    head = ListNode(1)
    current = head
    for i in lst:
        l = ListNode(i)
        current.next = l
        current = l
    return head.next

if __name__ == "__main__":
    s = Solution()
    l1 = list_2_node([2,4,3])
    l2 = list_2_node([5,6,4])
    res = s.addTwoNumbers(l1, l2)
    a = 1

    l1 = list_2_node([5])
    l2 = list_2_node([5])
    res = s.addTwoNumbers(l1, l2)
    a = 1