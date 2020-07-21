# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isStartWithRoot(self, head: ListNode, root: TreeNode) -> bool:
        # start with root node
        if not head:
            return True
        if not root:
            return False
        if root.val == head.val:
            is_left_ok = self.isStartWithRoot(head.next, root.left)
            if is_left_ok:
                return True
            is_right_ok = self.isStartWithRoot(head.next, root.right)
            if is_right_ok:
                return True
        return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        if self.isStartWithRoot(head, root):
            return True
        is_left_ok = self.isSubPath(head, root.left)
        if is_left_ok:
            return True
        is_right_ok = self.isSubPath(head, root.right)
        if is_right_ok:
            return True
        return False
