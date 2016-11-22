class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_num = [0, 0, 1]
        if n <= 2:
            return min_num[n]
        else:
            if n % 2 == 0:
                return 1 + self.integerReplacement(n//2)
            else:
                add = 2 + self.integerReplacement((n+1)//2)
                minus = 2 + self.integerReplacement((n-1)//2)
                min_num.append(min(add, minus))
                return min(add, minus)

if __name__ == "__main__":
    s = Solution()
    print(s.integerReplacement(7))
    print(s.integerReplacement(10000000))
