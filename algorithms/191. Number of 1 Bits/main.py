class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_1 = 0
        while n > 0:
            if n % 2 == 1:
                total_1 += 1
            n = n >> 1
        return total_1

if __name__ == "__main__":
    s = Solution()
    print s.hammingWeight(6)