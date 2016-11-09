class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        five = 0
        while n > 1:
            five += n / 5
            n /= 5
        return five

if __name__ == "__main__":
    s = Solution()
    print s.trailingZeroes(10)

