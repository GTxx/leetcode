# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def startroot(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            if root.val == sum:
                return 1
            else:
                return 0
        else:
            res = 1 if root.val == sum else 0
            if root.left:
                n = self.startroot(root.left, sum-root.val)
                res += n
            if root.right:
                n = self.startroot(root.right, sum - root.val)
                res += n
            return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = 0
        # include root
        n = self.startroot(root, sum)
        res += n

        # not include root
        if root.left:
            n = self.pathSum(root.left, sum)
            res += n
        if root.right:
            n = self.pathSum(root.right, sum)
            res += n
        return res
