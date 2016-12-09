class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = [1,1,2]
            for i in range(3, n+1):
                total = 0
                for j in range(i):
                    total += res[j] * res[i-1-j]
                res.append(total)
            return res[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))

