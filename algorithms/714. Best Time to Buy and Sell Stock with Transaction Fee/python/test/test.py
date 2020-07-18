from solution import Solution


def test():
    s = Solution()
    assert s.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert s.maxProfit([1, 1, 1], 2) == 0
    assert s.maxProfit([1, 2, 3], 2) == 0
    assert s.maxProfit([1, 2, 4], 2) == 1
    assert s.maxProfit([1, 3, 5, 4, 2, 9, 8], 2) == 7
