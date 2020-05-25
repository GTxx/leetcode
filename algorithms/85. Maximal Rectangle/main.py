from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def get_left_smaller_idx(idx, value):
            left_index = idx - 1
            while left_index >= 0:
                if heights[left_index] >= value:
                    left_index = left_smaller[left_index]
                else:
                    break
            return left_index

        def get_right_smaller_idx(idx, value):
            right_index = idx + 1
            while right_index < len(heights):
                if heights[right_index] >= value:
                    right_index = right_smaller[right_index]
                else:
                    break
            return right_index

        left_smaller = [0 for _ in range(len(heights))]
        right_smaller = [0 for _ in range(len(heights))]

        for idx, height in enumerate(heights):
            left_smaller_idx = get_left_smaller_idx(idx, height)
            left_smaller[idx] = left_smaller_idx
        for idx, height in reversed(list(enumerate(heights))):
            right_smaller_idx = get_right_smaller_idx(idx, height)
            right_smaller[idx] = right_smaller_idx
        max_area = 0
        for idx, height in enumerate(heights):
            area = height * (right_smaller[idx] - left_smaller[idx] - 1)
            max_area = max(area, max_area)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        width = len(matrix[0])
        histgram = [0 for _ in range(width)]
        max_area = 0
        for row in matrix:
            for idx, value in enumerate(row):
                if value == "0":
                    histgram[idx] = 0
                else:
                    histgram[idx] += 1
            area = self.largestRectangleArea(histgram)
            max_area = max(max_area, area)
        return max_area


if __name__ == "__main__":
    s = Solution()
    rect = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    assert s.maximalRectangle(rect) == 6
