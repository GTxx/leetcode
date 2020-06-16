from main import Solution

data = [
    [
        [1, 2, 3, 4, 6],
        [3, 5, 10, 6, 9],
        [20, 20, 100, 70, 60],
        150
    ]
]


def test_dp():
    s = Solution()
    for startTime, endTime, profit, result in data:
        assert s.jobScheduling1(startTime, endTime, profit) == result


def test_recursive():
    s = Solution()
    for startTime, endTime, profit, result in data:
        assert s.jobScheduling(startTime, endTime, profit) == result
