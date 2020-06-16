class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = first_one_idx = 0
        last_one_idx = len(nums) - 1
        while start <= last_one_idx:
            if nums[start] == 1:
                start += 1
            elif nums[start] == 0:
                if start > first_one_idx:
                    nums[start] = nums[first_one_idx]
                    nums[first_one_idx] = 0
                start += 1
                first_one_idx += 1
            else: # == 2
                if start <= last_one_idx:
                    nums[start] = nums[last_one_idx]
                    nums[last_one_idx] = 2
                    last_one_idx -= 1
