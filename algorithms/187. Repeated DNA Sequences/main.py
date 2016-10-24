class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ten_letter_set = set()
        duplicate_set = set()
        for idx in range(len(s) - 9):
            if s[idx: idx+10] in ten_letter_set:
                duplicate_set.add(s[idx: idx+10])
            else:
                ten_letter_set.add(s[idx: idx+10])
        return list(duplicate_set)


if __name__ == "__main__":
    s = Solution()
    print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print s.findRepeatedDnaSequences("AAAAAAAAAAA")
