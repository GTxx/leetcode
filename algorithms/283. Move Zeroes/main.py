from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        non_zero_idx = 0
        idx = 0
        while non_zero_idx < len(nums):
            if nums[non_zero_idx] == 0:
                non_zero_idx += 1
                zero_num += 1
            else:
                nums[idx] = nums[non_zero_idx]
                idx += 1
                non_zero_idx += 1

        for i in range(idx, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums)
    assert nums == [1,3,12,0,0]
    nums = []
    s.moveZeroes(nums)
    assert nums == []
    nums = [0]
    s.moveZeroes(nums)
    assert nums == [0]


