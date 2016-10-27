class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = [-prices[0]] * len(prices)
        sell = [-float('inf')] * len(prices)
        cool = [0] * len(prices)

        for idx, price in enumerate(prices[1:], 1):
            buy[idx] = max(cool[idx-1] - price, buy[idx-1])
            sell[idx] = buy[idx-1] + price
            cool[idx] = max(cool[idx-1], sell[idx-1])
        return max(cool[-1], sell[-1])


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1, 2, 3, 0, 2])

