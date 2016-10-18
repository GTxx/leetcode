# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

import heapq


class MyHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.val, node))

    def pop(self):
        return heapq.heappop(self.heap)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = MyHeap()
        for l in lists:
            if l:
                heap.push(l)

        start = ListNode(1)
        current_node = start
        while heap.heap:
            val, min_node = heap.pop()
            current_node.next = min_node
            current_node = current_node.next
            min_node = min_node.next
            if min_node:
                heap.push(min_node)
        return start.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n3
    n2.next = n4

    s = Solution()
    res = s.mergeKLists([n1, n2])

    res = s.mergeKLists([ListNode(0), ListNode(1)])
