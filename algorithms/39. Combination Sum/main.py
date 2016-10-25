class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]
        elif not candidates:
            return []
        elif target < min(candidates):
            return []
        else:
            res = []
            use_first = self.combinationSum(candidates, target-candidates[0])
            if use_first:
                res += [solution + [candidates[0]] for solution in use_first]

            no_use_first = self.combinationSum(candidates[1:], target)
            if no_use_first:
                res += no_use_first
            return res


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
    print s.combinationSum([1], 2)
