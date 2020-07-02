from solution import Solution

def test():
    s = Solution()
    assert s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]) == 5
    assert s.lenLongestFibSubseq([1,3,7,11,12,14,18]) == 3
