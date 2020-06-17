from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev = nums[0]
        up = None
        res = 1
        for num in nums[1:]:
            if num > prev and up is not True:
                up = True
                res += 1
            elif num < prev and up is not False:
                up = False
                res += 1
            prev = num
        return res
