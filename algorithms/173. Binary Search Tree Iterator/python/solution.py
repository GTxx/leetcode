# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [] # used to store node with bigger value
        current = root
        while current:
            self.stack.append(current)
            current = current.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        current = self.stack.pop()
        res = current.val
        current = current.right
        while current:
            self.stack.append(current)
            current = current.left
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()