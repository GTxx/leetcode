class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        real_idx = 0
        for idx, num in enumerate(nums):
            if nums[real_idx] == nums[idx]:
                continue
            else:
                real_idx += 1
                nums[real_idx] = nums[idx]
        return real_idx + 1


if __name__ == "__main__":
    s = Solution()
    l = [1,1,2]
    print s.removeDuplicates(l)
    print l
    l = []
    print s.removeDuplicates(l)
    print(l)
    l = [1,2]
    print s.removeDuplicates(l)
    print(l)


