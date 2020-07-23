from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            l = []
            i1 = i
            for idx, num in enumerate(nums):
                rem = i1 % 2
                i1 = i1 >> 1
                if rem == 1:
                    l.append(num)
            res.append(l)
        return res
