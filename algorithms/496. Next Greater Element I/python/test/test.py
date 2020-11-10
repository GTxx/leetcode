from ..main import Solution


def test1():
    s = Solution()
    assert s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]) == [-1, 3, -1]
