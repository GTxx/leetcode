class Solution(object):
    def threeSum(self, nums):
        """
        this solution is time out
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res_3 = []
        for idx, num in enumerate(nums):
            res_2 = self.two_sum(nums[idx+1:], -num)
            if res_2:
                for res in res_2:
                    l = [num] + res
                    if l not in res_3:
                        res_3.append(l)
        return res_3

    def two_sum(self, nums, target):
        res = []
        for idx, num in enumerate(nums):
            for num1 in nums[idx+1:]:
                if num + num1 == target:
                    if [num, num1] not in res:
                        res.append([num, num1])
                    break
        return res

    def threeSum1(self, nums):
        """ threeSum1 and threeSum2 can pass judge, both cost almost the same time"""
        nums = sorted(nums)
        res = []
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1 + 1:], idx1 + 1):
                if -num1 - num2 in nums[idx2+1: ]:
                    if [num1, num2, -num1-num2] not in res:
                        res.append([num1, num2, -num1-num2])
        return res

    def threeSum2(self, nums):
        nums = sorted(nums)
        res = []
        length1 = len(nums)
        for idx1 in range(length1):
            for idx2 in range(idx1+1, length1):
                num1 = nums[idx1]
                num2 = nums[idx2]
                num3 = -num1 - num2
                if num3 in nums[idx2 + 1: ]:
                    if [num1, num2, num3] not in res:
                        res.append([nums[idx1], nums[idx2], -nums[idx1]-nums[idx2]])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
    # assert(s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]])
    print(
        s.threeSum1([0,-6,0,-14,2,0,-9,5,-9,-8,-7,12,-4,14,-6,6,0,5,-2,6,-7,1,10,-10,-5,3,-2,-3,-13,-6,1,-6,3,9,-5,12,-6,-7,2,0,1,11,-11,4,2,-2,-5,-13,11,0,9,11,-13,-4,-13,-11,14,-8,1,8,1,9,-13,-11,3,-11,9,12,-2,-4,-11,6,14,-7,-5,1,-1,-3,-4,-5,12,12,13,6,-7,-15,10,14,14,-12,8,0,13,2,-3,1,-1,-9,-9,12,-6,-5,-5,-6,4,5,2,10,-13,13,12,6])
    )
