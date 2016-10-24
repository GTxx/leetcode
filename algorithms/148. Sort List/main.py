# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use merge sort

        def merge_sorted_2_list(l1, l2):
            head = ListNode(None)
            current = head
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
            if l2:
                current.next = l2
            return head.next

        def get_list_len(lst):
            if not lst:
                return 0
            i = 0
            while lst:
                i += 1
                lst = lst.next
            return i

        def split_lst(lst):
            length = get_list_len(lst)
            half = length / 2
            head = lst
            for i in range(half-1):
                lst = lst.next

            rest = lst.next
            lst.next = None
            return head, rest

        if not head:
            return None
        if not head.next:
            return head

        l1, l2 = split_lst(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        res = merge_sorted_2_list(l1, l2)
        return res


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
    res = s.sortList(l)

    l = list_2_nodes([3, 7])
    res = s.sortList(l)

    l = list_2_nodes([3])
    res = s.sortList(l)

    a = 1
