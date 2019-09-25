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

    def twoSum1(self, nums, target):
        for idx, num in enumerate(nums):
            rem = target - num
            if rem in nums[idx+1: ]:
                return [idx, nums[idx+1: ].index(rem) + idx + 1]
        return None
    
    def twoSum2(self, nums, target):
        map = {}
        for idx, num in enumerate(nums):
            rem = target - num
            if map.get(rem) is not None:
                return [map.get(rem), idx]
            else:
                map[num] = idx 


if __name__ == "__main__":
    s = Solution()
    assert(s.twoSum([2, 7, 11, 15], 9) == [0, 1])
    assert(s.twoSum([3, 2, 4], 6) == [1, 2])

    assert(s.twoSum1([2, 7, 11, 15], 9) == [0, 1])
    assert(s.twoSum1([3, 2, 4], 6) == [1, 2])

    assert(s.twoSum2([2, 7, 11, 15], 9) == [0, 1])
    assert(s.twoSum2([3, 2, 4], 6) == [1, 2])
