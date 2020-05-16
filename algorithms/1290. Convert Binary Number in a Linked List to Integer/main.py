# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(0)
    n3 = ListNode(1)
    n1.next = n2
    n2.next = n3

    s = Solution()
    assert s.getDecimalValue(n1) == 5
