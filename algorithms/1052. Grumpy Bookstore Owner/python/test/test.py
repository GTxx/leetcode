from solution import Solution


def test():
    s = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X= 3
    assert s.maxSatisfied(customers, grumpy, X) == 16