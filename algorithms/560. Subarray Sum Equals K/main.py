from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum -> count, represent how many times a sum value appears
        sum_count = {0: 1}
        sum_it = 0
        count = 0
        for num in nums:
            sum_it += num
            if sum_count.get(sum_it -k):
               count += sum_count.get(sum_it - k)
            if sum_count.get(sum_it):
                sum_count[sum_it] = sum_count[sum_it] + 1
            else:
                sum_count[sum_it] = 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1,1,1], 2) == 2
    assert s.subarraySum([], 2) == 0
    assert s.subarraySum([1,2,3,1,1,1], 6) == 3

