from typing import List


class Solution:
    def recursive(self, M, piles: List[int], total: int) -> int:
        # Time limit exceed where piles length > 20
        if len(piles) <= 2 * M:
            return total
        res = 0
        for i in range(1, 2 * M + 1):
            first_i = sum(piles[: i])
            rest = total - first_i
            max_can_get = rest - self.recursive(max(i, M), piles[i:], rest)
            res = max(res, max_can_get + first_i)
        return res

    def stoneGameII1(self, piles: List[int]) -> int:
        return self.recursive(1, piles, sum(piles))

    def stoneGameII(self, piles: List[int]) -> int:
        dp = [[] for _ in range(len(piles))]  # dp[i][j] represent max value can be taken from piles[i:] when M = j
        total = 0
        for idx in reversed(range(len(piles))):
            total += piles[idx]
            M = 1
            while M * 2 < len(piles) - idx:
                M_max = 0
                for i in range(1, 2 * M + 1):
                    take_first_i = sum(piles[idx: idx + i])
                    next_M = max(i, M)
                    if next_M >= len(dp[idx+i]):
                        rest_can_take = total - take_first_i - dp[idx+i][-1]
                    else:
                        rest_can_take = total - take_first_i - dp[idx + i][next_M-1]
                    M_max = max(M_max, take_first_i + rest_can_take)
                dp[idx].append(M_max)
                M += 1
            if M * 2 >= len(piles) - idx:
                dp[idx].append(total)
        return dp[0][0]
