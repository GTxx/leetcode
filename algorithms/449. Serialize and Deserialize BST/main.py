import json


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return json.dumps(self.to_dict(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self.dict_to_node(json.loads(data))

    def to_dict(self, root: TreeNode) -> dict:
        if not root: return {}
        d = {"val": root.val}
        if root.left:
            left_dict = self.to_dict(root.left)
            d['left'] = left_dict
        if root.right:
            right_dict = self.to_dict(root.right)
            d['right'] = right_dict
        return d

    def dict_to_node(self, d: dict) -> 'TreeNode':
        if d:
            n = TreeNode(d['val'])
            if d.get("left"):
                n.left = self.dict_to_node(d['left'])
            if d.get("right"):
                n.right = self.dict_to_node(d['right'])
            return n
        else:
            return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    codec = Codec()
    s = codec.serialize(n1)
    nn = codec.deserialize(s)
    assert nn.val == 1
    assert nn.left.val == 2
