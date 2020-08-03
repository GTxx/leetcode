# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longest_same_value_from_root(self, root: TreeNode, val: int) -> int:
        if root and root.val == val:
            left_len = self.longest_same_value_from_root(root.left, val)
            right_len = self.longest_same_value_from_root(root.right, val)
            return 1 + max(left_len, right_len)
        else:
            return 0

    def longest_pass_root(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_len = self.longest_same_value_from_root(root.left, root.val)
        right_len = self.longest_same_value_from_root(root.right, root.val)
        return 1 + left_len + right_len

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        pass_root = self.longest_pass_root(root)
        if pass_root > 0:
            pass_root -= 1
        left_len = self.longestUnivaluePath(root.left)
        right_len = self.longestUnivaluePath(root.right)
        res = max(pass_root, left_len, right_len)
        return res
