from functools import cmp_to_key
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s_n = [i for i in range(1, n+1)]
        s_n.sort(key=cmp_to_key(self.compare))
        return s_n

    def compare(self, i: int, j: int):
        if str(i) < str(j):
            return -1
        elif str(i) > str(j):
            return 1
        else:
            return 0