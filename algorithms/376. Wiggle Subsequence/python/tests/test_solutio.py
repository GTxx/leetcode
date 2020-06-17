from main import Solution


def test_solution():
    s = Solution()
    assert s.wiggleMaxLength([1,7,4,9,2,5]) == 6
    assert s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
    assert s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2
    assert s.wiggleMaxLength([1, 1, 1]) == 1
    assert s.wiggleMaxLength([1, 1, 2]) == 2
    assert s.wiggleMaxLength([]) == 0
