from typing import List


class Solution:
    def get_divisor(self, num, dividend):
        if num % dividend == 0:
            return num // dividend
        else:
            return (num - num % dividend) // dividend + 1

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sum_nums = sum(nums)
        min_result = self.get_divisor(sum_nums, threshold) - 1
        max_result = max(nums)
        current = (min_result + max_result) // 2
        while max_result > min_result + 1:
            sum_divisor = 0
            for num in nums:
                sum_divisor += self.get_divisor(num, current)
            if sum_divisor <= threshold:
                max_result = current
                current = (min_result + max_result) // 2
            else:
                min_result = current
                current = (min_result + max_result) // 1
        return max_result

