from solution import Solution


def test():
    s = Solution()
    assert s.canReorderDoubled([3, 1, 3, 6]) == False
    assert s.canReorderDoubled([2, 1, 2, 6]) == False
    assert s.canReorderDoubled([4, -2, 2, -4]) == True
    assert s.canReorderDoubled([4, -2, 2, -5]) == False
    assert s.canReorderDoubled([1, 2, 4, 16, 8, 4]) == False
