from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        min_value = 1000000
        max_value = -1000000
        origin_diff = 0
        for i, j in zip(nums, nums[1:]):
            min_value = min(min_value, max(i, j))
            max_value = max(max_value, min(i, j))
            origin_diff += abs(i -j)
        if max_value > min_value:
            res = origin_diff + abs(max_value - min_value) * 2
        else:
            res = origin_diff

        if len(nums) >=3:
            first = nums[0]
            last = nums[-1]
            for idx in range(1, len(nums) -1):
                if first < nums[idx] < nums[idx+1] or first > nums[idx] > nums[idx+1]:
                    res = max(res, origin_diff + abs(nums[idx]-first))
                if nums[idx-1] < nums[idx] < last or nums[idx-1] > nums[idx] > last:
                    res = max(res, origin_diff + abs(nums[idx] - last))
        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.maxValueAfterReverse([2,3,1,5,4]))
    print(s.maxValueAfterReverse([1,2,3]))
    print(s.maxValueAfterReverse([2,4,9,24,2,1,10]))
    print(s.maxValueAfterReverse([1]))
    print(s.maxValueAfterReverse([1,2]))
    print(s.maxValueAfterReverse([]))
