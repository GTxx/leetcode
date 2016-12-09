class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def _combine(candidates, target):
            if target == 0:
                return [()]
            elif not candidates:
                return []
            elif target < min(candidates):
                return []
            else:
                res = set()
                use_first = _combine(candidates[1:], target-candidates[0])
                if use_first:
                    for i in use_first:
                        res.add((candidates[0], ) + i)

                no_use_first = _combine(candidates[1:], target)
                if no_use_first:
                    for i in no_use_first:
                        res.add(i)

                return list(res)

        candidates = sorted(candidates)

        return [list(i) for i in _combine(candidates, target)]


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)