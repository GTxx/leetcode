# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree1(self, inorder, postorder):

        def _build(start_in, end_in, start_post, end_post):
            if start_in == end_in:
                return None
            root_val = postorder[end_post-1]
            root_node = TreeNode(root_val)

            idx = inorder[start_in: end_in].index(root_val)
            left_start_in = start_in
            left_end_in = start_in + idx
            left_start_post = start_post
            left_end_post = start_post + idx
            left = _build(left_start_in, left_end_in, left_start_post, left_end_post)

            right_start_in = start_in + idx + 1
            right_end_in = end_in
            right_start_post = start_post + idx
            right_end_post = end_post - 1
            right = _build(right_start_in, right_end_in, right_start_post, right_end_post)
            root_node.left = left
            root_node.right = right
            return root_node
        return _build(0, len(inorder), 0, len(postorder))

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode

        this solution can not pass judge, memory limit exceeded
        """
        if not inorder:
            return None

        root_val = postorder[-1]
        root_node = TreeNode(root_val)
        idx = inorder.index(root_val)
        left_inorder = inorder[: idx]
        right_inorder = inorder[idx+1:]
        left_postorder = postorder[: idx]
        right_postorder = postorder[idx: -1]
        left = self.buildTree(left_inorder, left_postorder)
        right = self.buildTree(right_inorder, right_postorder)
        root_node.left = left
        root_node.right = right
        return root_node