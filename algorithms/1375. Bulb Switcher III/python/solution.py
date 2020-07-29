from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        lighted = set()
        blued = set()
        res = 0
        for l in light:
            lighted.add(l)
            if l == 1 or l - 1 in lighted:
                blued.add(l)
            if l + 1 in lighted and l + 1 not in blued:
                blued.add(l+1)
            if len(blued) == len(lighted):
                res += 1
        return res
