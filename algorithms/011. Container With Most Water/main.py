from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        left_height = height[left]
        right_height = height[right]
        area = min(left_height, right_height) * (right - left)
        while left < right:
            left_to_right = True if height[left] <= height[right] else False
            if left_to_right:
                while left < right:
                    left += 1
                    if height[left] > left_height:
                        left_height = height[left]
                        break
            else:
                while left < right:
                    right -= 1
                    if height[right] > right_height:
                        right_height = height[right]
                        break
            area = max(area, min(left_height, right_height) * (right - left))
        return area



if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
