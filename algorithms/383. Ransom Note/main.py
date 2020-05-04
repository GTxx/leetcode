class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_lst = list(ransomNote)
        magazine_lst = list(magazine)
        for letter in ransom_lst:
            if letter in magazine_lst:
                magazine_lst.remove(letter)
            else:
                return False
        return True

    def canConstruct1(self, ransomNote, magazine):
        d = {}
        for c in magazine:
            if d.get(c):
                d[c] += 1
            else:
                d[c] = 1
        for c in ransomNote:
            if d.get(c):
                if d[c] >= 1:
                    d[c] -= 1
                else:
                    return False
            else:
                return False
        return True



if __name__ == "__main__":
    from algorithms import test
    s = Solution()
    test(('a', 'b'), False, s.canConstruct)
    test(('aa', 'ab'), False, s.canConstruct)
    test(('aa', 'aab'), True, s.canConstruct)

    test(('a', 'b'), False, s.canConstruct1)
    test(('aa', 'ab'), False, s.canConstruct1)
    test(('aa', 'aab'), True, s.canConstruct1)