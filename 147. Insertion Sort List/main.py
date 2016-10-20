# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        list_head = ListNode(-float('inf'))
        list_head.next = head
        current = list_head

        while True:
            if not current.next:
                break
            if current.val > current.next.val:
                next = current.next
                current.next = current.next.next
                current1 = list_head.next
                prev = list_head
                while True:
                    if current1.val > next.val:
                        next.next = current1
                        prev.next = next
                        break
                    else:
                        current1 = current1.next
                        prev = prev.next
            else:
                current = current.next
        return list_head.next


def list_2_nodes(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in lst[1:]:
        n = ListNode(i)
        current.next = n
        current = current.next
    return head

if __name__ == "__main__":
    s = Solution()
    l = list_2_nodes([3, 7, 4, 9, 5, 2, 6, 1])
    res = s.insertionSortList(l)
    a = 1
