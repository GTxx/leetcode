class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = float('inf')
        max_diff = 0
        for idx, price in enumerate(prices):
            min_buy = min(min_buy, price)
            max_diff = max(max_diff, price - min_buy)
        return max_diff

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([1])
