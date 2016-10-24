class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = [word for word in s.split(" ") if word]
        return " ".join(reversed(word_list))


if __name__ == "__main__":
    s = Solution()
    assert(s.reverseWords("the sky is blue") == "blue is sky the")
    assert(s.reverseWords(" ") == "")
