class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        if not word_list:
            return 0
        else:
            return len(word_list[-1])