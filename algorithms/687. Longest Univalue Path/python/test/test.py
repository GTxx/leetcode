from solution import Solution, TreeNode


def build_tree(lst):
    root = TreeNode(lst[0])
    current_row = [root]
    idx = 1
    while idx < len(lst):
        next_row = []
        for node in current_row:
            if node and idx < len(lst):
                node.left = TreeNode(lst[idx]) if lst[idx] else None
                next_row.append(node.left)
            else:
                next_row.append(None)
            idx += 1
            if node and idx < len(lst):
                node.right = TreeNode(lst[idx]) if lst[idx] else None
                next_row.append(node.right)
            else:
                next_row.append(None)
            idx += 1
        current_row = next_row
    return root


def test():
    tree = build_tree([1,4,5,4,4,5])
    s = Solution()
    assert s.longestUnivaluePath(tree) == 2
