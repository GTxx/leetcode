class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        for letter in s:
            t.remove(letter)
        return t[0]


if __name__ == "__main__":
    s = Solution()
    print s.findTheDifference('abcd', 'abcde')

