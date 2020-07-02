from solution import Solution


def test():
    s = Solution()
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537
