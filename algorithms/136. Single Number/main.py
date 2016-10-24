class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x^y, nums, 0)


if __name__ == "__main__":
    s = Solution()
    assert(s.singleNumber([1,2,2,3,3]) == 1)
    assert(s.singleNumber([1,2,2,3,3]) == 1)
