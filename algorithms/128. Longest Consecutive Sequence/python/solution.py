from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = {}
        res = 0
        for num in nums:
            if num in dct:
                continue
            else:
                if num-1 in dct:
                    left_size = dct[num-1]
                else:
                    left_size = 0
                if num + 1 in dct:
                    right_size = dct[num+1]
                else:
                    right_size = 0
                total_size = left_size + right_size + 1
                res = max(res, total_size)
                dct[num] = total_size
                dct[num-left_size] = total_size
                dct[num+right_size] = total_size
        return res
