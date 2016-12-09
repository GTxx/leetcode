class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_first_n = [0]
        max_first_n[0] = nums[0]
        for idx, num in enumerate(nums[1:], 1):
            if max_first_n[idx-1] < 0:
                max_first_n.append(num)
            else:
                max_first_n.append(max_first_n[idx-1] + num)

        return max(max_first_n)



if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])