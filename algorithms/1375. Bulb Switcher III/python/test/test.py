from solution import Solution

def test():
    s = Solution()
    assert s.numTimesAllBlue([2,1,3,5,4]) == 3
    assert s.numTimesAllBlue([3,2,4,1,5]) == 2
    assert s.numTimesAllBlue([4,1,2,3]) == 1
    assert s.numTimesAllBlue([2,1,4,3,6,5]) == 3
    assert s.numTimesAllBlue([1,2,3,4,5,6]) == 6
