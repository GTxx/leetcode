class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]

        d1, d2 = 0, 1
        r, c = 0, 0
        for i in range(1, n*n+1):
            res[r][c] = i
            if res[(r+d1)%n][(c+d2)%n]:
                d1, d2 = d2, -d1
            r += d1
            c += d2
        return res

if __name__ == "__main__":
    s = Solution()
    print s.generateMatrix(3)


