from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in row ] for row in obstacleGrid]
        for idx, val in reversed(list(enumerate(obstacleGrid[-1]))):
            if val == 0:
                dp[-1][idx] = 1
            else:
                break
        for idx, row in reversed(list(enumerate(obstacleGrid))):
            if row[-1] == 0:
                dp[idx][-1] = 1
            else:
                break
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        for h in range(height-2, -1, -1):
            all_zero = False if dp[h][-1] == 1 else True
            for w in range(width-2, -1, -1):
                if obstacleGrid[h][w] == 0:
                    dp[h][w] = dp[h+1][w] + dp[h][w+1]
                    if dp[h][w] != 0:
                        all_zero = False
            if all_zero:
                break
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    m = [
  [0,0,0],
  [0,1,1],
  [0,0,0]
]
    print(s.uniquePathsWithObstacles(m))
    m = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(s.uniquePathsWithObstacles(m))
