class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y: x ^ y, nums, 0)

        not_zero_bitwise = xor & -xor

        first_group = [num for num in nums if num & not_zero_bitwise != 0 ]
        second_group = [num for num in nums if num & not_zero_bitwise == 0]

        first = reduce(lambda x, y: x ^ y, first_group, 0)
        second = reduce(lambda x, y: x ^ y, second_group, 0)
        return first, second


if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1,2,1,3,2,5])
