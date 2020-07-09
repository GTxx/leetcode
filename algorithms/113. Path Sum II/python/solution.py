# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root.left and not root.right:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        res = []
        if root.left:
            for path in self.pathSum(root.left, sum - root.val):
                res.append([root.val] + path)
        if root.right:
            for path in self.pathSum(root.right, sum - root.val):
                res.append([root.val] + path)
        return res
