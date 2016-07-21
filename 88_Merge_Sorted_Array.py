class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[0:m] + nums2[0:n]
        nums3.sort()
        for i in range(len(nums1)):
            nums1.pop()
        for ele in nums3:
            nums1.append(ele)


if __name__ == "__main__":
    s = Solution()
    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    print(nums1)
