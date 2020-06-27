from solution import Solution


def test():
    s = Solution()
    assert s.removePalindromeSub("ababa") == 1
    assert s.removePalindromeSub("abb") == 2
    assert s.removePalindromeSub("baabb") == 2
