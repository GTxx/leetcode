class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest / minutesToDie + 1
        pigs = 1
        total = times
        while total < buckets:
            total *= times
            pigs += 1
        return pigs

if __name__ == "__main__":
    s = Solution()
    print(s.poorPigs(1000, 15, 60))
