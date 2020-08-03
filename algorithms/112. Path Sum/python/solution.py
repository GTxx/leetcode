# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            if sum == 0:
                return True
            else:
                return False
        if (not root.left or not root.right) and root.val == sum:
            return True
        if root.left:
            if self.hasPathSum(root.left, sum - root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, sum - root.val):
                return True
        return False

