class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = None
        end = None
        res = []
        for num in nums:
            if start is None:
                start = end = num
            else:
                if num - end == 1:
                    end = num
                else:
                    if start == end:
                        res.append("{}".format(start))
                    else:
                        res.append("{}->{}".format(start, end))
                    start = end = num

        if start is not None:
            if start == end:
                res.append("{}".format(start))
            else:
                res.append("{}->{}".format(start, end))

        return res

if __name__ == "__main__":
    s = Solution()
    print s.summaryRanges([0,1,2,4,5,7])
    print s.summaryRanges([])
    print s.summaryRanges([0, 1])
