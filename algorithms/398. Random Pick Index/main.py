class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        n = 0
        rem = None
        for idx, num in enumerate(self.nums):
            if num == target:
                n += 1
                if random.random() < 1.0 / n:
                    rem = idx
        return rem

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)