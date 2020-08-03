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
    s = Solution()
    root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    # assert s.startroot(root.right, 8) == 1
    assert s.startroot(root.left, 8) == 2
    assert s.pathSum(root, 8) == 3
