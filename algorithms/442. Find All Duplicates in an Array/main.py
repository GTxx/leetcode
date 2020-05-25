from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0
        res = []
        while idx < len(nums):
            num = nums[idx]
            if num == idx + 1:
                nums[idx] = -num
                idx += 1
                continue
            if num < 0:
                idx += 1
                continue
            if nums[num - 1] > 0:
                tmp = nums[num - 1]
                nums[num - 1] = -num
                nums[idx] = tmp
                continue
            elif nums[num - 1] == 0:
                nums[idx] = 0
                nums[num - 1] = -num
                idx += 1
                continue
            else:
                nums[idx] = 0
                res.append(num)
                idx += 1
        return res


if __name__ == "__main__":
    s = Solution()
    from algorithms import test

    # ass
    assert set(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == {3, 2}
    assert set(s.findDuplicates([3, 11, 8, 16, 4, 15, 4, 17, 14, 14, 6, 6, 2, 8, 3, 12, 15, 20, 20, 5])) == {4, 14, 6,
                                                                                                              8, 3, 15,
                                                                                                              20}
