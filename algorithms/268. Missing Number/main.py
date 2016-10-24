class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        length = len(nums)
        total = (length+1)*length/2
        return total - sum(nums)


if __name__ == "__main__":
    s = Solution()
    print s.missingNumber([0,1,3])
    print s.missingNumber([0,1,2])
