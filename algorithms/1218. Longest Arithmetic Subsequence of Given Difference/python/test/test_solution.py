from main import Solution

data = [
    [[1, 2, 3, 4], 1, 4],
    [[1, 3, 5, 7], 1, 1],
    [[1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4]
]


def test_solution():
    s = Solution()
    for lst, diff, result in data:
        assert s.longestSubsequence(lst, diff) == result
