# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_head.next = head
        current = new_head
        idx = 0
        while True:
            idx += 1
            if idx < m:
                current = current.next
            else:
                break

        m_tail = current
        m_head = current.next
        m_prev = None
        m_next = m_head
        while True:
            if idx <= n:
                idx += 1
                m_prev1, m_next1 = m_next, m_next.next
                m_next.next = m_prev
                m_prev, m_next = m_prev1, m_next1
            else:
                break
        if m_prev:
            m_tail.next = m_prev
            m_head.next = m_next

        return new_head.next

if __name__ == "__main__":
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    res = s.reverseBetween(n1, 2, 4)
    n1 = ListNode(3)
    n2 = ListNode(5)
    n1.next = n2
    res = s.reverseBetween(n1, 1, 2)
    a = 1

