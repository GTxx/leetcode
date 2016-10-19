# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        level_nodes = [root, ]
        while True:
            if not level_nodes:
                break
            new_level_nodes = []
            for node in level_nodes:
                if node.left:
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)

            level_nodes = new_level_nodes
        return res


