from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[0]
        sold = buy + fee
        total_profit = 0
        for price in prices[1:]:
            if price > sold:
                sold = price
            elif price < sold - fee:
                total_profit += sold - buy - fee
                buy = price
                sold = buy + fee
        total_profit += sold - buy - fee
        return total_profit