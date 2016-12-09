class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            numbers = [num for num in row if num != '.']
            if len(numbers) != len(set(numbers)):
                return False

        for col_i in range(len(board[0])):
            numbers = [board[row_i][col_i] for row_i in range(len(board))
                       if board[row_i][col_i] != '.']
            if len(numbers) != len(set(numbers)):
                return False

        for i in range(3):
            for j in range(3):
                numbers = []
                for ii in range(3):
                    for jj in range(3):
                        if board[i*3+ii][j*3+jj] != '.':
                            numbers.append(board[i*3+ii][j*3+jj])

                if len(numbers) != len(set(numbers)):
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    board = [".87654321","8........","3........","4........","5........","6........","7........","8........","9........"]
    print s.isValidSudoku(board)

