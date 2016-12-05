class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums) - 1
            while low != high:
                diff = nums[low] + nums[high] + nums[i] - target
                if diff == 0:
                    return target
                elif diff > 0:
                    high -= 1
                else:
                    low += 1
                if abs(diff) < abs(closest - target):
                    closest = diff + target
        return closest

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 0, 0], 1))
    print(s.threeSumClosest([1, 1, 1, 0], 100))
    print(s.threeSumClosest([-3,-2,-5,3,-4], -1))

