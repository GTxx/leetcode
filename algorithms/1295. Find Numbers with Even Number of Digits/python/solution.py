from typing import List


class Solution:
    def is_even_number(self, num) -> int:
        if 10<= num < 100 or 1000<=num < 10000 or 100000 <= num < 1000000:
            return 1
        else:
            return 0

    def findNumbers(self, nums: List[int]) -> int:
        # 1 <= nums[i] <= 10^5
        return sum((self.is_even_number(num) for num in nums))

