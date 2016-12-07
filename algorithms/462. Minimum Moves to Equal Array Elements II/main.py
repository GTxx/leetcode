class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums) / 2]
        res = 0
        for num in nums:
            res += abs(num - mid)
        return res