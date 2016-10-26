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


if __name__ == "__main__":
    s = Solution()
    print s.canConstruct('a', 'b')
    print s.canConstruct('aa', 'ab')
    print s.canConstruct('aa', 'aab')
