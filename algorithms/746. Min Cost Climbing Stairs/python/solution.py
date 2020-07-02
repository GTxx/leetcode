from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []  # dp[i] represent the minimum cost from step i to the end
        for idx, c in enumerate(reversed(cost)):
            if idx <= 1:
                dp.append(c)
            else:
                min_cost = min(c + dp[idx-2], c + dp[idx - 1])
                dp.append(min_cost)
        return min(dp[-1], dp[-2])
