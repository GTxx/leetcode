class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        exp2 = 1
        for idx in xrange(num+1):
            if idx == 0:
                res.append(0)
            elif idx == 1:
                res.append(1)
            else:
                if idx >= exp2 * 2:
                    exp2 = exp2 * 2
                res.append(1+res[idx-exp2])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.countBits(5)
