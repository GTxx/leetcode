from collections import deque
from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = [i for i in range(0, 10)]
        for _ in range(N - 1):
            length = len(res)
            for idx in range(length):
                value = res[idx]
                if value == 0:
                    continue
                last_num = value % 10
                for new_last_num in [i for i in range(10) if last_num + K == i or last_num - K == i]:
                    res.append(new_last_num + value * 10)
            res = res[length:]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.numsSameConsecDiff(3, 7) == [181, 292, 707, 818, 929]
    assert s.numsSameConsecDiff(2, 1) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    assert s.numsSameConsecDiff(1, 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert s.numsSameConsecDiff(1, 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
