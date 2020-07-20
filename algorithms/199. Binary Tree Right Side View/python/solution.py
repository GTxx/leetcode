# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        lst = [root]
        res = []
        while len(lst) != 0:
            res.append(lst[-1].val)
            next_lst = []
            for node in lst:
                if node.left:
                    next_lst.append(node.left)
                if node.right:
                    next_lst.append(node.right)
            lst = next_lst
        return res



