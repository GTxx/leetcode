from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        appeared_char = set()
        uniq_chars = OrderedDict()
        for index, c in enumerate(s):
            if c not in appeared_char:
               uniq_chars[c] = index
               appeared_char.add(c)
            else:
                if c in uniq_chars:
                    uniq_chars.pop(c)
        if len(uniq_chars) == 0:
            return -1
        else:
            return uniq_chars.popitem(last=False)[1]


if __name__ == "__main__":
    from algorithms import test
    s = Solution()
    test("leetcode", 0, s.firstUniqChar)
    test("loveleetcode", 2, s.firstUniqChar)
