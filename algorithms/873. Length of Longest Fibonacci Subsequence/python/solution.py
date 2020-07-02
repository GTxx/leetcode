from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        set_a = set(A)
        res = 0
        first, second = 0, 1
        while first < len(A) - max(2, res):
            second = first + 1
            while second < len(A) - max(1, res-1):
                cnt = 0
                i, j = A[first], A[second]
                while i+j in set_a:
                    i, j = j, i+j
                    cnt += 1
                if cnt != 0:
                    res = max(res, cnt+2)
                second += 1
            first += 1
        return res

