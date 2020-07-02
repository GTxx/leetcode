from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strenght = []
        for idx, row in enumerate(mat):
            row_strenght.append((sum(row), idx))
        row_strenght.sort(key=lambda x: (x[0], x[1]))
        return [row for _, row in row_strenght[:k]]


if __name__ == "__main__":
    s = Solution()
    mat =[[1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]]
    assert s.kWeakestRows(mat, 3) == [2, 0, 3]
    mat = [[1, 0, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0]]
    assert s.kWeakestRows(mat, 2) == [0, 2]