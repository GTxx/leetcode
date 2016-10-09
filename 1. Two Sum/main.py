class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            for idx1, num1 in enumerate(nums[idx+1:], idx+1):
                if num + num1 == target:
                    return [idx, idx1]

        return None


if __name__ == "__main__":
    s = Solution()
    assert(s.twoSum([2, 7, 11, 15], 9) == [0, 1])
    assert(s.twoSum([3, 2, 4], 6) == [1, 2])
