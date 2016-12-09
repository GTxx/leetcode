class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            else:
                max_reach = max(i+nums[i], max_reach)
        return True


if __name__ == "__main__":
    s = Solution()
    print s.canJump([2,3,1,1,4])
    print s.canJump([3,2,1,0,4])

