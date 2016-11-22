class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        for idx, c in enumerate(citations, 1):
            if idx > c:
                return idx - 1
        return idx


if __name__ == "__main__":
    s = Solution()
    print s.hIndex([1,2,3,3])
    print s.hIndex([3,0,6,1,5])
    print s.hIndex([0])

