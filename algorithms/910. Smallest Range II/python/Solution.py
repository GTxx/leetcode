from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return 0
        A.sort()
        res = A[-1] - A[0]
        for i, a in enumerate(A[:-1]):
            current_min = min(A[0] + K, A[i+1] - K)
            current_max = max(A[-1] - K, a + K)
            diff = current_max - current_min
            if diff < res:
                res = diff
        return res



