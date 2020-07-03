from solution import Solution


def test():
    s = Solution()
    assert s.numMovesStones(4, 3, 2) == [0, 0]
    assert s.numMovesStones(3, 5, 1) == [1, 2]
    assert s.numMovesStones(3, 4, 1) == [1, 1]
    assert s.numMovesStones(40, 100, 1) == [2, 97]
