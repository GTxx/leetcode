# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return -1
        else:
            left_second_min = self.findSecondMinimumValue(root.left)
            right_second_min = self.findSecondMinimumValue(root.right)
            min_list = [root.val, root.left.val, root.right.val, left_second_min, right_second_min]
            min_list = [i for i in min_list if i != -1]
            if len(set(min_list)) <= 1:
                return -1
            else:
                min_list.sort()
                min_val = min_list[0]
                for val in min_list[1:]:
                    if val != min_val:
                        return val
