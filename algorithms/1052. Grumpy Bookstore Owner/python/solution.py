from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = sum(customers[:X])
        for customer, g in zip(customers[X:], grumpy[X:]):
            if g == 0:
                total += customer
        max_total = total
        for i in range(1, len(customers) - X + 1):
            if grumpy[i-1] == 1:
                total = total - customers[i-1]
            if grumpy[i+X-1] == 1:
                total = total + customers[i+X-1]
            max_total = max(max_total, total)
        return max_total

