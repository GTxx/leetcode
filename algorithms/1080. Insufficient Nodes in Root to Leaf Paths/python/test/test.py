from solution import Solution, TreeNode


def test():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(-99)
    n6 = TreeNode(-99)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n10 = TreeNode(-99)
    n11 = TreeNode(-99)
    n12 = TreeNode(12)
    n13 = TreeNode(13)
    n14 = TreeNode(-99)
    n15 = TreeNode(14)
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11
    n6.left = n12
    n6.right = n13
    n7.left = n14
    n7.right = n15
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n1.left = n2
    n1.right = n3
    s = Solution()
    res = s.sufficientSubset(n1, 1)
    assert res.left.right is None
