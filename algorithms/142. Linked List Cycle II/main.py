# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while True:
            if head is None:
                return None
            else:
                if head in visited:
                    return head
                else:
                    visited.add(head)
                    head = head.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n2

    s = Solution()
    assert(s.detectCycle(n1) == n2)