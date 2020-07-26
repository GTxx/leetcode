# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rec(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif left is not None and right is not None and left.val == right.val:
            if left.left is None and left.right is None and right.left is None and right.right is None:
                return True
            return self.rec(left.left, right.right) and self.rec(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.rec(root.left, root.right)

    def isSymmetric1(self, root: TreeNode) -> bool:
        current_depth = [root]
        while current_depth:
            vals = [node.val if node else None for node in current_depth]
            if vals != vals[::-1]:
                return False
            next_depth = []
            all_none = True
            for node in current_depth:
                if node:
                    if node.left or node.right:
                        all_none = False
                    next_depth.append(node.left)
                    next_depth.append(node.right)
                else:
                    next_depth.append(None)
                    next_depth.append(None)
            current_depth = next_depth
            if all_none:
                break
        return True

