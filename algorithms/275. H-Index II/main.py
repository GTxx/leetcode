class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if len(citations) == 1:
            return min(1, citations[0])
        low = 0
        high = len(citations) - 1
        c_len = len(citations)
        while low <= high:
            mid = (low + high) / 2
            if c_len - mid > citations[mid]:
                low = mid + 1
            elif c_len - mid <= citations[mid]:
                if c_len - mid + 1 > citations[mid-1]:
                    return c_len - mid
                else:
                    high = mid - 1
        return c_len - low

if __name__ == "__main__":
    s = Solution()
    print s.hIndex([])
    print s.hIndex([1])
    print s.hIndex([0])
    print s.hIndex([0, 1,3,5,6])
    print s.hIndex([0, 0])
    print s.hIndex([99, 100])
    print s.hIndex([0, 0, 1])
