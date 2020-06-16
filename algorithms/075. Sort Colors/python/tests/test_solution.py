from main import Solution

data = [
    [[2, 0, 1], [0, 1, 2]],
    [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],
    [[1, 1, 1, 0, 2, 1, 1], [0, 1, 1, 1, 1, 1, 2]],
    [[], []],
    [[0], [0]],
    [[1], [1]],
    [[2], [2]],
    [[2, 2], [2, 2]],
    [[0, 1, 0], [0, 0, 1]],
]


def test():
    s = Solution()
    for input, result in data:
        s.sortColors(input)
        assert input == result
