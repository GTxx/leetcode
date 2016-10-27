class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy1 = [-prices[0]] * len(prices)
        sell1 = [-float('inf')] * len(prices)
        buy2 = [-float('inf')] * len(prices)
        sell2 = [-float('inf')] * len(prices)

        for idx, price in enumerate(prices[1:], 1):
            buy1[idx] = max(buy1[idx-1], -price)
            sell1[idx] = max(sell1[idx-1], buy1[idx-1] + price)
            buy2[idx] = max(buy2[idx-1], sell1[idx-1] - price)
            sell2[idx] = max(buy2[idx-1] + price, sell2[idx-1])
        return max(sell1+sell2+[0])


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1,2,3,4])