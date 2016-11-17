class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def _solve(start, k, n):
            if start > 9:
                return []
            if k == 1:
                if start <= n <= 9:
                    return [[n]]
                else:
                    return []
            else:
                res = []
                for i in range(start, 10):
                    solution = _solve(i+1, k-1, n-i)
                    if solution:
                        for s in solution:
                            res.append([i]+s)
                return res

        return _solve(1, k, n)

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum3(3, 7)
    print s.combinationSum3(3, 9)
