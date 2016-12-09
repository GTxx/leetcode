class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        row, col = 0, 0
        dr, dc = 0, 1
        row_len, col_len = len(matrix), len(matrix[0])
        res = []
        for _ in range(row_len* col_len):
            res.append(matrix[row][col])
            matrix[row][col] = None
            if matrix[(row+dr)%row_len][(col+dc)%col_len] is None:
                dr, dc = dc, -dr
            row += dr
            col += dc
        return res

if __name__ =="__main__":
    a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    s = Solution()
    print s.spiralOrder(a)