class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def _combine(lst, k):
            if k == 0:
                return []
            elif k == 1:
                return [[i] for i in lst]
            elif len(lst) < k:
                return []
            elif len(lst) == k:
                return [lst]
            else:
                res = []
                first = lst[0]
                use_first = _combine(lst[1:], k-1)
                res += [[first] + i for i in use_first]

                no_use_first = _combine(lst[1:], k)
                res += no_use_first
                return res
        return _combine(range(1, n+1), k)

if __name__ == "__main__":
    s = Solution()
    print s.combine(4, 2)