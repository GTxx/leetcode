class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1) + 1
        len_2 = len(word2) + 1
        dp = [[0 for _ in range(len_1)] for _ in range(len_2)]
        for i in range(len_1):
            dp[0][i] = i
        for i in range(len_2):
            dp[i][0] = i
        for i in range(1, len_2):
            for j in range(1, len_1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    replace = 1 + dp[i-1][j-1]
                    remove_i = 1 + dp[i-1][j]
                    remove_j = 1 + dp[i][j-1]
                    dp[i][j] = min(replace, remove_i, remove_j)
        return dp[len_2-1][len_1-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("1", "1") == 0
    assert s.minDistance("12", "1") == 1
    assert s.minDistance("12", "1") == 1
    assert s.minDistance("", "") == 0
    assert s.minDistance("", "1") == 1
    assert s.minDistance("plasma", "altruism") == 6
