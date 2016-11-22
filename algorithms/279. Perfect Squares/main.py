class Solution(object):
    _dp = []
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gen_squre(n):
            i = 2
            while i * i <= n:
                yield i * i
                i += 1
        for i in range(len(self._dp), n+1):
            min_num_square = i
            for j in gen_squre(i):
                if min_num_square > 1 + self._dp[i-j]:
                    min_num_square = 1 + self._dp[i-j]
            self._dp.append(min_num_square)

        return self._dp[n]


if __name__ =="__main__":
    s = Solution()
    print s.numSquares(12)
    print s.numSquares(13)
    print s.numSquares(230)
    print s.numSquares(5778)
