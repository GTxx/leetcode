# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        current_level = [root]
        res = []
        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    res.append(node.val)
                    left = node.left if node.left else None
                    next_level.append(left)
                    right = node.right if node.right else None
                    next_level.append(right)
                else:
                    res.append(None)
            current_level = next_level

        # trim null in the end
        while res[-1] is None:
            res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def get_data(data):
            d = {'idx': 0}
            def _next():
                try:
                    val = data[d['idx']]
                    d['idx'] += 1
                    return val
                except Exception:
                    return None
            return _next

        if not data:
            return None

        next_data = get_data(data)
        root = TreeNode(next_data())
        current_level = [root]

        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    left_val = next_data()
                    if left_val is not None:
                        left = TreeNode(left_val)
                        node.left = left
                        next_level.append(left)

                    right_val = next_data()
                    if right_val is not None:
                        right = TreeNode(right_val)
                        node.right = right
                        next_level.append(right)
            current_level = next_level
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = None
    n1.right = n2
    n2.left = n3
    n2.right = None

    c = Codec()
    res = c.serialize(n1)
    print(res)
    root = c.deserialize(res)
    print root

    root = c.deserialize([-1,0,3,-2,4,None,None,8])
    print root

    root = c.deserialize([10,9,11,8,None,None,12,7,None, None,13,6,None,None,14,
                          5,None,None,15,4,None,None,16,3,None,None,17,2,None,
                          None,18,1,None,None,19,0])
    res = c.serialize(root)
    print res
