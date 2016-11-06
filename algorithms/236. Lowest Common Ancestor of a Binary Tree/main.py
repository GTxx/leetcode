# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
                    if left_path:
                        return [root] + left_path
                if root.right:
                    right_path = find(root.right, node)
                    if right_path:
                        return [root] + right_path
                return []

        p_path = find(root, p)
        q_path = find(root, q)
        idx = 0
        while True:
            try:
                if p_path[idx] == q_path[idx]:
                    idx += 1
                else:
                    break
            except Exception:
                break
        return p_path[idx-1]

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2
    s = Solution()
    res = s.lowestCommonAncestor(n1, n1, n2)
    print res

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    res = s.lowestCommonAncestor(n1, n2, n3)
    print res


