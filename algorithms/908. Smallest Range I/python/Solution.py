from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_val = min(A)
        max_val = max(A)
        if max_val - min_val >= K * 2:
            return max_val - min_val - K * 2
        else:
            return 0
