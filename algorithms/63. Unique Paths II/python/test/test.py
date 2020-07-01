from solution import Solution


def test():
    s = Solution()
    m = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    assert s.uniquePathsWithObstacles(m) == 1
    m = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert s.uniquePathsWithObstacles(m) == 2