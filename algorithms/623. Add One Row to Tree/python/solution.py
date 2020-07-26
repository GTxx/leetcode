# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return None
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        elif d == 2:
            new_left = TreeNode(v)
            if root.left:
                new_left.left = root.left
            root.left = new_left
            new_right = TreeNode(v)
            if root.right:
                new_right.right = root.right
            root.right = new_right
        else:
            left = self.addOneRow(root.left, v, d-1)
            right = self.addOneRow(root.right, v, d - 1)
            root.left = left
            root.right = right
        return root

