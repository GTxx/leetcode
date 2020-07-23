from solution import Solution


def test():
    s = Solution()
    assert len(s.subsets([1, 2, 3])) == 8
