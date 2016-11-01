import math


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_nums = len(matrix)
        col_nums = len(matrix[0])

        def rotate_row_num(row, col, row_c, col_c):
            x, y = row - row_c, col-col_c
            x, y = y, -x
            return int(x + row_c), int(y + col_c)

        row_c = (row_nums - 1) / 2.0
        col_c = (col_nums - 1) / 2.0
        for row in range(row_nums/2):
            for col in range(int(math.ceil(col_nums/2.0))):
                row2, col2 = rotate_row_num(row, col, row_c, col_c)
                row3, col3 = rotate_row_num(row2, col2, row_c, col_c)
                row4, col4 = rotate_row_num(row3, col3, row_c, col_c)
                temp = matrix[row][col]
                matrix[row][col] = matrix[row4][col4]
                matrix[row4][col4] = matrix[row3][col3]
                matrix[row3][col3] = matrix[row2][col2]
                matrix[row2][col2] = temp


if __name__ == "__main__":
    s = Solution()
    m = [[1,2,3], [4,5,6], [7,8,9]]
    s.rotate(m)
    print m