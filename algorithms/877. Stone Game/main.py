from typing import List


def get_max(piles, start, end) -> int:
    if start == end:
        return piles[start]
    if start + 1 == end:
        return max(piles[start], piles[end])
    else:
        pick_left = piles[start] + min(get_max(piles, start + 1+1, end), get_max(piles, start + 1, end - 1))
        pick_right = piles[end] + min(get_max(piles, start + 1, end - 1), get_max(piles, start, end - 2))
        return max(pick_left, pick_right)


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return get_max(piles, 0, len(piles) - 1) * 2 > sum(piles)

    def stoneGame1(self, piles: List[int]) -> bool:
        dp = [[0 for _ in piles] for _ in piles]
        for i, value in enumerate(piles):
            dp[i][i] = value
        sum = [0]
        total = 0
        for i in piles:
            total += i
            sum.append(total)
        for j in range(1, len(piles)):
            for i in range(0, len(piles) - j):
                pick_left = piles[i] + sum[i + j + 1] - sum[i + 1] - dp[i + 1][i + j]
                pick_right = piles[i + j] + sum[i + j] - sum[i] - dp[i][i + j - 1]
                dp[i][i + j] = max(pick_left, pick_right)
        return dp[0][len(piles) - 1] * 2 > sum[len(piles)]


if __name__ == "__main__":
    s = Solution()
    from algorithms import test

    test([[5, 3, 5, 4], 0, 3], 10, get_max)
    test([[3, 5, 4], 0, 2], 7, get_max)
    test([[5, 3], 0, 1], 5, get_max)
    test([[3], 0, 0], 3, get_max)

    test([[5, 3, 5, 4]], True, s.stoneGame)
    test([[4, 3, 5]], True, s.stoneGame)
    test([[5, 3]], True, s.stoneGame)
    test([[3]], True, s.stoneGame)

    test([[5, 3, 5, 4]], True, s.stoneGame1)
    test([[4, 3, 5]], True, s.stoneGame1)
    test([[5, 3]], True, s.stoneGame1)
    test([[3]], True, s.stoneGame1)
