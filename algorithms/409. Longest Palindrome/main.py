class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        c_set = set()
        for c in s:
            if c in c_set:
                res += 2
                c_set.remove(c)
            else:
                c_set.add(c)
        if len(c_set) > 0:
            return res + 1
        else:
            return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))

