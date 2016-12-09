class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        current = ''
        for c in s:
            if c in current:
                current = current.split(c)[1]
            current += c
            if len(current) > longest:
                longest = len(current)
        return longest

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("dvdf")