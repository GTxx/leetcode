class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = list(sorted(nums))
        res = []
        for idx1, num1 in enumerate(nums):
            rem1 = nums[idx1+1:]
            if len(rem1) < 3:
                break
            if sum(rem1[:3]) + num1 > target:
                break
            if sum(rem1[-3:]) + num1 < target:
                continue

            for idx2, num2 in enumerate(nums[idx1+1:], idx1+1):
                rem2 = nums[idx2+1: ]
                if len(rem2) < 2:
                    break
                if (sum(rem2[:2])) + num1 + num2 > target:
                    break
                if (sum(rem2[-2:])) + num1 + num2 < target:
                    continue

                for idx3, num3 in enumerate(nums[idx2+1: ], idx2+1):
                    rem3 = nums[idx3+1: ]
                    if len(rem3) < 1:
                        break
                    if rem3[0] + num1 + num2 + num3 > target:
                        break
                    if rem3[-1] + num1 + num2 + num3 < target:
                        continue

                    num4 = target -num1 - num2 - num3
                    if self.bi_search(nums[idx3 + 1: ], num4) is not None and\
                        [num1, num2, num3, num4] not in res:
                        res.append([num1, num2, num3, num4])

        return res

    def bi_search(self, nums, num):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == num:
                return mid
            elif nums[mid] > num:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def fourSum1(self, nums, target):
        pass

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))