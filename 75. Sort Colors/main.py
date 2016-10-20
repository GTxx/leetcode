class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        no_zero_idx = 0
        no_second_idx = len(nums) - 1
        start = 0
        while start < no_second_idx:
            while nums[start] == 2 and start < no_second_idx:
                nums[start] = nums[no_second_idx]
                nums[no_second_idx] = 2
                no_second_idx -= 1
            while nums[start] == 0 and start > no_zero_idx:
                nums[start] = nums[no_zero_idx]
                nums[no_zero_idx] = 0
                no_zero_idx += 1
            start += 1
        return nums


if __name__ == "__main__":
    s = Solution()
    assert(s.sortColors([0,1,1,0,2,2]) == [0, 0, 1, 1, 2, 2])
    assert(s.sortColors([]) == [])
    res = s.sortColors([])
    s.sortColors([0, 0])
    a = 1
