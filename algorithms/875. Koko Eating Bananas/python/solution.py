from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)
        # m1: non-working value, m2: Ok value
        m1, m2 = 1, ceil(max(piles) * len(piles) / H)
        while m1 < m2 - 1:
            mid = (m1 + m2) // 2
            cost_hour = sum([ceil(i/mid) for i in piles])
            if cost_hour <= H:
                m2 = mid
            else:
                m1 = mid
        return m2


