class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for r in row:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        for c in col:
            for r in range(len(matrix)):
                matrix[r][c] = 0


if __name__ == "__main__":
    s = Solution()
    m = [
        [0, 1, 1],
        [1,1,1],
        [1,0,1]
    ]
    s.setZeroes(m)
    print(m)

    m = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    s.setZeroes(m)
    print(m)
