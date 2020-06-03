from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        rec1 ovelap rec2 only when width of rec1 overlap width or rec2, and
        height of rec1 overlap height of rec2
        :param rec1:
        :param rec2:
        :return:
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        return (x11 < x22 and x21 < x12) and (y11 < y22 and y21 < y12)


if __name__ == "__main__":
    s = Solution()
    assert s.isRectangleOverlap([7,8,13,15], [10,8,12,20]) is True
    assert s.isRectangleOverlap([0,0,2,2], [1,1,3,3]) is True
    assert s.isRectangleOverlap([0,0,1,1], [1,0,2,1]) is False

