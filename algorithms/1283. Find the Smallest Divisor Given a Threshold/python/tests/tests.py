from main import Solution

def test():
    s = Solution()
    assert s.smallestDivisor([1,2,5,9], 6) == 5
    assert s.smallestDivisor([2,3,5,7,11], 11) == 3
    assert s.smallestDivisor([2,2,2,2], 4) == 2
