class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        addon = []
        total = 0
        addon.append(total)
        for i in nums:
            total += i
            addon.append(total)
        self.addon = addon

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.addon[j+1] - self.addon[i]


# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    numArray = NumArray([1,2,3,4])
    print(numArray.sumRange(0, 1))
    print(numArray.sumRange(1, 2))
