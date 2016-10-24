# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        level_nodes = [root, ]
        while True:
            if not level_nodes:
                break
            level_vals = []
            new_level_nodes = []
            for node in level_nodes:
                level_vals.append(node.val)
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            res.append(level_vals)
            level_nodes = new_level_nodes
        return res

def list_2_tree(lst):
    root = TreeNode(lst[0])
    idx_lst = [0]
    level_node_lst = [root, ]
    while True:
        if not idx_lst:
            break
        new_idx_lst = []
        new_level_node_lst = []
        for idx, node in zip(idx_lst, level_node_lst):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            if left_idx < len(lst) and lst[left_idx]:
                left_node = TreeNode(lst[left_idx])
                node.left = left_node
                new_idx_lst.append(left_idx)
                new_level_node_lst.append(left_node)
            if right_idx < len(lst) and lst[right_idx]:
                right_node = TreeNode(lst[right_idx])
                node.right = right_node
                new_idx_lst.append(right_idx)
                new_level_node_lst.append(right_node)
        idx_lst = new_idx_lst
        level_node_lst = new_level_node_lst
    return root

if __name__ == "__main__":
    tree = list_2_tree([3,9,20,None,None,15,7])
    s = Solution()
    res = s.levelOrder(tree)
    true_res = [[3],
                [9,20],
                [15,7]]
    assert(res == true_res)
