class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_larger_idx(x, nums, start_idx):
            idx_lst = []
            for idx, num in enumerate(nums, start_idx):
                if x < num:
                   idx_lst.append(idx)
            return idx_lst

        if not nums:
            return 0
        max_length = [0] * len(nums)
        for idx in reversed(range(len(nums))):
            num = nums[idx]
            larger_idx_lst = find_larger_idx(num, nums[idx+1:], idx+1)
            if not larger_idx_lst:
                max_length[idx] = 1
            else:
                max_length[idx] = 1 + max([max_length[larger_idx] for larger_idx in larger_idx_lst])
        return max(max_length)


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLIS([10, 9,2,5,3,7,101, 18])
