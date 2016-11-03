# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def _build(pre_start, pre_end, in_start, in_end):
            if pre_start == pre_end:
                return None

            root_val = preorder[pre_start]
            idx = inorder[in_start: in_end].index(root_val)
            root_node = TreeNode(root_val)
            left_node = _build(pre_start+1, pre_start+1+idx, in_start, in_start+idx)
            right_node = _build(pre_start+idx+1, pre_end, in_start+idx+1, in_end)
            root_node.left = left_node
            root_node.right = right_node
            return root_node
        return _build(0, len(preorder), 0, len(inorder))

    def buildTruee(self, preorder, inorder):
        """ memory limit exceeded %>_<%"""
        if not preorder:
            return None

        root = preorder[0]
        idx = inorder.index(root)
        # left_inorder = inorder[:idx]
        # right_inorder = inorder[idx+1:]
        # left_preorder = preorder[1: idx+1]
        # right_preorder = preorder[idx+1:]

        root_node = TreeNode(root)
        left_node = self.buildTree(preorder[1: idx + 1], inorder[:idx])
        right_node = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        root_node.left = left_node
        root_node.right = right_node
        return root_node