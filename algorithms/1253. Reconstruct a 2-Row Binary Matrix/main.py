from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper > len(colsum) or lower > len(colsum):
            return []
        if upper + lower != sum(colsum):
            return []
        res = [[0 for _ in range(len(colsum))] for _ in range(2)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
                upper -= 1
        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper != 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
        if upper != 0:
            return []
        else:
            return res


if __name__ == "__main__":
    s = Solution()
    res = s.reconstructMatrix(2, 1, [1, 1, 1])
    assert sum(res[0]) == 2
    assert sum(res[1]) == 1
    assert res[0][0] + res[1][0] == 1

    assert [] == s.reconstructMatrix(2, 3, [2, 2, 1, 1])

    res = s.reconstructMatrix(5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1])
    assert sum(res[0]) == 5
    assert sum(res[1]) == 5

    print(s.reconstructMatrix(9, 2, [0,1,2,0,0,0,0,0,2,1,2,1,2]))
