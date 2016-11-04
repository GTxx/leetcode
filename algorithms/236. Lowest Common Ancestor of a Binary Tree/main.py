# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find(root, node):
            if root == node:
                return [node]
            elif not root:
                return []
            else:
                if root.left:
                    left_path = find(root.left, node)
                    if not left_path:
                        return []
                    else:
                        return [root] + left_path
                if root.right:
                    right_path = find(root.right, node)
                    if not right_path:
                        return []
                    else:
                        return [root] + right_path
                return []

        p_path = find(root, p)
        q_path = find(root, q)
        idx = 0
        while p_path[idx] == q_path[idx]:
            idx += 1
        return p_path[idx-1]





