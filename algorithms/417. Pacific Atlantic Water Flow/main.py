class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        row_len = len(matrix)
        col_len = len(matrix[0])

        def _mark(f_matrix, start_point):
            r, c = start_point
            r_c_lst = [(r1, c1) for r1, c1 in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if
                       0 <= r1 < row_len and 0 <= c1 < col_len and f_matrix[r1][c1] is False]
            res = []
            for r1, c1 in r_c_lst:
                if matrix[r1][c1] >= matrix[r][c] and f_matrix[r1][c1] == False:
                    res.append((r1, c1))
                    f_matrix[r1][c1] = True
            if not res:
                return
            else:
                for r1, c1 in res:
                    _mark(f_matrix, (r1, c1))


        pacific_matrix = [[False] * col_len for _ in range(row_len)]

        start_points = []
        for i in range(col_len):
            pacific_matrix[0][i] = True
            start_points.append((0, i))

        for i in range(1, row_len):
            pacific_matrix[i][0] = True
            start_points.append((i, 0))

        for start_point in start_points:
            _mark(pacific_matrix, start_point)

        atlantic_matrix = [[False] * col_len for _ in range(row_len)]
        start_points = []
        for i in range(col_len):
            atlantic_matrix[row_len-1][i] = True
            start_points.append((row_len-1, i))
        for i in range(0, row_len-1):
            atlantic_matrix[i][col_len-1] = True
            start_points.append((i, col_len-1))
        for start_point in start_points:
            _mark(atlantic_matrix, start_point)

        res = []
        for r in range(row_len):
            for c in range(col_len):
                if pacific_matrix[r][c] == True and atlantic_matrix[r][c] == True:
                    res.append([r, c])
        return res


if __name__ == "__main__":
    s = Solution()
    matrix= [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    res = s.pacificAtlantic(matrix)
    matrix = [[1,2,2,1], [2,1,2,1], [2,1,2,1],[2,1,1,1]]
    res = s.pacificAtlantic(matrix)
