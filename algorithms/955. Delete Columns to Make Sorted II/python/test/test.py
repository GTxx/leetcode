from solution import Solution

def test():
    s = Solution()
    assert s.minDeletionSize(["ca", "bb", "ac"]) == 1
    assert s.minDeletionSize(["az", "by", "cd"]) == 0
    assert s.minDeletionSize(["xga","xfb","yfa"]) == 1
