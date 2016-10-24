class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.arg = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            self.arg[idx + 1] = self.arg[idx] + nums[idx]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i: j+1])


        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)

    def sumRange1(self, i, j):
        return self.arg[j+1] - self.arg[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    s = NumArray(nums)
    assert(s.sumRange1(0, 2) == 1)
