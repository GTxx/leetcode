class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            rob_first = nums[0] + self.rob_list(nums[2:-1])
            rob_no_first = self.rob_list(nums[1:])
            return max(rob_first, rob_no_first)

    def rob_list(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            max_rob = [nums[0], max(nums[:2])]
            for i in range(2, len(nums)):
                rob_last = nums[i] + max_rob[i - 2]
                not_rob_last = max_rob[i - 1]
                max_rob.append(max(rob_last, not_rob_last))
            return max_rob[-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.rob([1,2,3,4,5]), 8)