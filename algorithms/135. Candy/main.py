class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1

        res = [1] * len(ratings)
        for idx in range(len(ratings)-1):
            prev = ratings[idx]
            next = ratings[idx+1]
            if next > prev:
                res[idx+1] = res[idx] + 1
        for idx in reversed(range(1, len(ratings))):
            prev = ratings[idx]
            next = ratings[idx-1]
            if next > prev and res[idx-1] <= res[idx]:
                res[idx-1] = res[idx] + 1
        return sum(res)

if __name__ == "__main__":
    s = Solution()
    print s.candy([0])
    print s.candy([1,2,3])
    print s.candy([1,1])
    print s.candy([5,1,1,1,10,2,1,1,1,3])
    a = range(1, 12001)
    a.reverse()
    print s.candy(a)
    print s.candy([4,2,3,4,1])
