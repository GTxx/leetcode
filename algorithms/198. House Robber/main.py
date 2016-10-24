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
            max_rob = [nums[0], max(nums[:2])]
            for i in range(2, len(nums)):
                rob_last = nums[i] + max_rob[i-2]
                not_rob_last = max_rob[i-1]
                max_rob.append(max(rob_last, not_rob_last))
            return max_rob[-1]

if __name__ == "__main__":
    s = Solution()
    print s.rob([1,2,3,4,5])

    print s.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165])
