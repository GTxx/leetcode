# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _find(nums, root):
            if not root:
                return []
            else:
                if root.left is None and root.right is None:
                    return [nums+[root.val]]
                else:
                    left = _find(nums+[root.val], root.left)
                    right = _find(nums+[root.val], root.right)
                    return left+right

        nums = _find([], root)
        res = 0
        for num in nums:
            res += int("".join(str(i) for i in num))
        return res


if __name__ == "__main__":
    s = Solution()
    assert(s.sumNumbers(TreeNode(0)) == 0)