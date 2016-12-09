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
                return [queens]
            positions = _find_pos(queens)
            if not positions:
                return None
            else:
                res = []
                for pos in positions:
                    solutions = _solve(queens + [pos], )
                    if solutions:
                        for s in solutions:
                            res.append(s)
                return res

        def to_str(queens):
            res = []
            for queen in queens:
                r, c = queen
                a = ["."] * n
                a[c] = 'Q'
                res.append("".join(a))
            return res

        solutions = _solve([])
        res = []
        for s in solutions:
            res.append(to_str(s))
        print(len(res))
        return res

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
    print s.solveNQueens(8)
