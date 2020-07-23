from solution import Solution


def test():
    s = Solution()
    assert set(s.letterCasePermutation("a1b2")) == {"a1b2", "a1B2", "A1b2", "A1B2"}
    assert set(s.letterCasePermutation("3z4")) == {"3z4", "3Z4"}
    assert set(s.letterCasePermutation("12345")) == {"12345"}
