from Solution import Solution

def test():
    s = Solution()
    assert s.smallestRangeII([1], 0) == 0
    assert s.smallestRangeII([0, 10], 2) == 6
    assert s.smallestRangeII([1,3,6], 3) == 3
    assert s.smallestRangeII([1,4,4,6], 3) == 3
