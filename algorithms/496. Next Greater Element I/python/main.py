from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_greater = [[num, -1]for num in nums2 ]
        for idx in reversed(range(len(nums2)-1)):
            if nums2[idx+1] > nums2[idx]:
               num_greater[idx][-1] = nums2[idx+1]
            else:
                for i in range(idx+1, len(nums2)):
                    if num_greater[idx][0] < num_greater[i][-1]:
                        num_greater[idx][-1] = num_greater[i][-1]
                        break
                else:
                    num_greater[idx][-1] = -1

        dct = {}
        for num, greater in num_greater:
            dct[num] = greater
        return [dct[num] for num in nums1]


if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]) == [-1, 3, -1]
    assert s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]) == [3, -1]
    assert s.nextGreaterElement(nums1=[135, 59, 92, 122, 52, 131, 236], nums2=[135, 59, 92, 122, 52, 131, 236]) \
           == [236,92,122,131,131, 236,-1]
