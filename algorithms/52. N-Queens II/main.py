class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def _find_pos(queens_pos):
            row = len(queens_pos)
            dead_col = []
            for queen_pos in queens_pos:
                r, c = queen_pos
                dead_col.append(c)
                dead_col.append(c + row - r)
                dead_col.append(c - row + r)
            dead_col = [c for c in dead_col if 0 <= c < n ]
            return [(row, c) for c in range(n) if c not in dead_col]

        def _solve(queens):
            if len(queens) == n:
                return 1
            positions = _find_pos(queens)
            if not positions:
                return 0
            else:
                res = 0
                for pos in positions:
                    solution_num = _solve(queens + [pos], )
                    res += solution_num
                return res

        return _solve([])

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
    print s.solveNQueens(8)