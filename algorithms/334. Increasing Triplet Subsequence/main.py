class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min = float('inf')
        middle = float('inf')
        for num in nums:
            if num <= min:
                min = num
            elif num <= middle:
                middle = num
            else:
                return True
        return False
