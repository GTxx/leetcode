class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = []
        for pre, after in zip(prices[:-1], prices[1:]):
            diff.append(after - pre)

        positive = [i for i in diff if i > 0]
        return sum(positive)


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1,2,3,4])