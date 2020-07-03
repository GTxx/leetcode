from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if b - a <= 1 and c - b <= 1:
            return [0, 0]
        elif b - a <= 2 or c - b <= 2:
            return [1, c - a - 2]
        else:
            return [2, c - a - 2]
