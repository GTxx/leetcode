from solution import Solution


def test():
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
