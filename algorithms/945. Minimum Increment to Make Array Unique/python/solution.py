from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        prev = A[0]
        res = 0
        for a in A[1:]:
            if prev + 1 > a:
                res += prev+1 - a
                prev = prev + 1
            else:
                prev = a
        return res

