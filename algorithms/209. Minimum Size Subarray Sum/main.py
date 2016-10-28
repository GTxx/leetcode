class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        """
        low, high, total = 0, -1, 0
        min_length = float('inf')
        for idx, num in enumerate(nums):
            total += num
            high = idx
            if total >= s:
                while total >= s:
                    total -= nums[low]
                    low += 1

                low -= 1
                total += nums[low]
                min_length = min(min_length, high-low+1)

        return 0 if min_length == float('inf') else min_length

if __name__ == "__main__":
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])
    print s.minSubArrayLen(11, [1,2,3,4,5])
    print s.minSubArrayLen(15, [1,2,3,4,5])
    print s.minSubArrayLen(6, [10,2,3])
