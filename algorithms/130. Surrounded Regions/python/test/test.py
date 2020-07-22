from solution import Solution


def test():
    s = Solution()
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # s.solve(board)
    # print(board)
    # board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    # s.solve(board)
    # print(board)
    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    s.solve1(board)
    assert board == [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
