# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flatten(root):
            if not root:
                return None
            left_flatten = _flatten(root.left)
            right_flatten = _flatten(root.right)
            root.left = None
            root.right = left_flatten
            leaf = root
            while leaf.right:
                leaf = leaf.right
            leaf.right = right_flatten
            return root
        _flatten(root)

if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    s.flatten(n1)

    n1 = TreeNode(1)
    s.flatten(n1)
    a = 1
