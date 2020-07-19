# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root.left and not root.right:
            if root.val < limit:
                return None
            else:
                return root
        else:
            left_node = right_node = None
            if root.left:
                left_node = self.sufficientSubset(root.left, limit - root.val)
            if root.right:
                right_node = self.sufficientSubset(root.right, limit - root.val)
            if not left_node and not right_node:
                return None
            root.left = left_node
            root.right = right_node
            return root
