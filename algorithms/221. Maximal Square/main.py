from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        h, w = len(matrix), len(matrix[0])
        get_result = [[0 for i in range(w)] for j in range(h)]

        def _get_max_area(i, j):
            if i == -1 or j == -1:
                return 0
            else:
                return get_result[i][j]

        max_area = 0
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == "0":
                    get_result[i][j] = 0
                else:
                    if _get_max_area(i, j - 1) >= _get_max_area(i - 1, j - 1) \
                            and _get_max_area(i - 1, j) >= _get_max_area(i - 1, j - 1):
                        get_result[i][j] = _get_max_area(i - 1, j - 1) + 1
                    else:
                        get_result[i][j] = 1 + min(_get_max_area(i - 1, j), _get_max_area(i, j - 1))
                max_area = max(max_area, get_result[i][j])
        return max_area


if __name__ == "__main__":
    s = Solution()
    input = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]
    input1 = [["0"]]
    # print(s.maximalSquare(input))
    print(s.maximalSquare(input1))
