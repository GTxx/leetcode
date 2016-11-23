# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = ListNode(None)
        second = ListNode(None)
        first.next = second
        second.next = head
        pre_node = first
        num = 1
        current = head
        current_val = None
        while current:
            if current.val != current_val:
                if num > 1:
                    pre_node.next = current
                else:
                    pre_node = pre_node.next
                current_val = current.val
                num = 1
            else:
                num += 1
            current = current.next
        if num > 1:
            pre_node.next = None
        return second.next

if __name__ == "__main__":
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    res = s.deleteDuplicates(n1)
    a = 1
