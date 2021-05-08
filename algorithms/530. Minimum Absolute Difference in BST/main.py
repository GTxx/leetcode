# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root == None:
            return None
        left_max = self.get_max(root.left)
        right_min = self.get_min(root.right)
        print("left_max: ",left_max)
        print("right_min", right_min)
        left_root_diff = root.val - left_max if left_max != None else None
        right_root_diff = right_min - root.val if right_min != None else None
        left_min_diff = self.getMinimumDifference(root.left)
        right_min_diff = self.getMinimumDifference(root.right)
        all_min = [i for i in [left_root_diff, right_root_diff, left_min_diff, right_min_diff] if i !=None]
        return min(all_min) if all_min else None

        
    def get_max(self, root: TreeNode) -> int:
        if root == None:
            return None
        while root.right != None:
            root = root.right
        return root.val
    
    def get_min(self, root: TreeNode) -> int:
        if root == None:
            return None
        while root.left != None:
            root = root.left
        return root.val

        
if __name__ == "__main__":
    root = TreeNode(5)
    left = TreeNode(2)
    right = TreeNode(6)
    root.left = left
    root.right = right
    left1 = TreeNode(1)
    left2 = TreeNode(3)
    left.left = left1
    left.right = left2

    s = Solution()
    assert s.getMinimumDifference(root) == 1