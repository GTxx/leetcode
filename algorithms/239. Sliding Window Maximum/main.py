class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_in_k = max(nums[:k])
        res = [max_in_k,]
        for i in range(1, len(nums) - k + 1):
            if nums[i+k-1] > max_in_k:
                max_in_k = nums[i+k-1]
            else:
                if nums[i-1] == max_in_k:
                    max_in_k = max(nums[i: i+k])

            res.append(max_in_k)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
