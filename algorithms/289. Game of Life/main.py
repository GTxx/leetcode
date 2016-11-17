class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row_len = len(board)
        col_len = len(board[0])
        live_set = set()
        for r in range(row_len):
            for c in range(col_len):
                neigh = 0
                for r1 in [i for i in [r-1, r, r+1] if 0<=i<row_len]:
                    for c1 in [i for i in [c-1, c, c+1] if 0<=i < col_len]:
                        if r1 != r or c1 != c:
                            if board[r1][c1] == 1:
                                neigh += 1

                if neigh == 2 and board[r][c] == 1:
                    live_set.add((r, c))
                elif neigh == 3:
                    live_set.add((r, c))

        for r in range(row_len):
            for c in range(col_len):
                if (r, c) not in live_set:
                    board[r][c] = 0
                else:
                    board[r][c] = 1


if __name__ == "__main__":
    s = Solution()
    b = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    s.gameOfLife(b)
    print(b)