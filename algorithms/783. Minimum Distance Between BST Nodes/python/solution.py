# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_value(self, root: TreeNode):
        while root.right:
            root = root.right
        return root.val

    def min_value(self, root: TreeNode):
        while root.right:
            root = root.left
        return root.val

    def minDiffInBST(self, root: TreeNode) -> int:
        res = 10000000
        if root.left:
            max_v = self.max_value(root.left)
            left_diff = self.minDiffInBST(root.left)
            res = min(res, root.val-max_v, left_diff)
        if root.right:
            min_v = self.min_value(root.right)
            right_diff = self.minDiffInBST(root.right)
            res = min(res, min_v-root.val, right_diff)
        return res

