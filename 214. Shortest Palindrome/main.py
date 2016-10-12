class Solution(object):

    def shortestPalindrome1(self, s):
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sufix = ""
        for i in xrange(len(s)):
            prefix = s[: len(s)-i]
            if self.is_palindrome(prefix):
                sufix = s[len(s) - i:]
                break

        return sufix[::-1] + s

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":

    import timeit
    s = Solution()

    # performance
    a = "a" * 20000 + 'c' + "a" *20001
    print(timeit.timeit(lambda: s.shortestPalindrome(a), number=1000))
    print(timeit.timeit(lambda: s.shortestPalindrome1(a), number=1000))
    assert(s.shortestPalindrome(a) == s.shortestPalindrome1(a))
