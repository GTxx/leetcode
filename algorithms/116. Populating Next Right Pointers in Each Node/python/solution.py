# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        lst = [root]
        while len(lst) != 0:
            for pre, next_node in zip(lst, lst[1:]+[None]):
                pre.next = next_node
            next_lst = []
            for node in lst:
                if node.left:
                    next_lst.append(node.left)
                if node.right:
                    next_lst.append(node.right)
            lst = next_lst
        return root
