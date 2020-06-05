from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        # left sequence num of value less then R
        left_less_num = 0
        # represent right most index with value in range(L, R)
        left_ok_len = 0
        res = 0
        for value in A:
            if L <= value <= R:
                left_less_num += 1
                res += left_less_num
                left_ok_len = 0
            elif value < L:
                left_ok_len += 1
                left_less_num += 1
                res += left_less_num - left_ok_len
            else:
                left_less_num = 0
                left_ok_len = 0
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3) == 3
    assert s.numSubarrayBoundedMax([], 2, 3) == 0
    assert s.numSubarrayBoundedMax([1, 2, 3, 4, 5], 2, 3) == 5
