# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        level_node = [root]
        while True:
            if None not in level_node:
                new_level_node = []
                all_none_child = True
                for node in level_node:
                    new_level_node.append(node.left)
                    new_level_node.append(node.right)
                    if node.left is not None or node.right is not None:
                        all_none_child = False
                if all_none_child:
                    return True
                level_node = new_level_node
            else:
                while len(level_node) != 0 and level_node[-1] is None:
                    level_node.pop()
                if None in level_node:
                    return False
                else:
                    for node in level_node:
                        if node.left is not None or node.right is not None:
                            return False
                    return True
