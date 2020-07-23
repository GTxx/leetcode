from typing import List
from collections import Counter
from itertools import product, chain


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        factors = []
        for num, cnt in counter.most_common():
            factor = []
            for i in range(cnt+1):
                factor.append([num for _ in range(i)])
            factors.append(factor)
        return [list(chain(*one)) for one in product(*factors)]




