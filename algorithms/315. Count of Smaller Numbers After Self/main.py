class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        class Node:
            def __init__(self, val, num):
                self.val = val
                self.num = num
                self.left_num = 0
                self.right = None
                self.left = None

        def insert_node(root, val):
            if not root:
                root = Node(val, 1)
            elif val == root.val:
                root.num += 1
            elif val > root.val:
                right = insert_node(root.right, val)
                root.right = right
            else:
                left = insert_node(root.left, val)
                root.left = left
                root.left_num += 1
            return root

        def get_smaller(root, val):
            if val == root.val:
                return root.left_num
            elif val > root.val:
                return root.num + root.left_num + get_smaller(root.right, val)
            else:
                return get_smaller(root.left, val)

        res = []
        root = None
        for num in reversed(nums):
            root = insert_node(root, num)
            smaller = get_smaller(root, num)
            res.append(smaller)

        res.reverse()
        return res


if __name__ == "__main__":
    s = Solution()
    assert(s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0])
    assert(s.countSmaller([0,2,1]) == [0, 1, 0])
    assert(s.countSmaller([6431,3945,9539,8608,9383,4757,1675,3448,3436,6238,7946,-369,-693,1382,9774]) ==
           [9, 6, 11, 9, 9, 6, 3, 4, 3, 3, 3, 1, 0, 0, 0])
    assert(s.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])==
           [10, 27, 10, 35, 12, 22, 28, 8, 19, 2, 12, 2, 9, 6, 12, 5, 17, 9, 19,
            12, 14, 6, 12, 5, 12, 3, 0, 10, 0, 7, 8, 4, 0, 0, 4, 3, 2, 0, 1, 0])
