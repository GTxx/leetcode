class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        while low <= high:
            if nums[high] == val:
                high -= 1
            elif nums[low] == val:
                nums[low] = nums[high]
                low += 1
                high -= 1
            else:
                low += 1

        return high+1

    def removeElement1(self, nums, val):
        while val in nums:
            nums.remove(val)
        return nums

if __name__ == "__main__":
    s = Solution()
    print s.removeElement([3,2,2,3], 3)
    print s.removeElement([3,3], 3)

