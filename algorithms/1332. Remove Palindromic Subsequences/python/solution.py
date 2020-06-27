class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True

    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        if self.is_palindrome(s):
            return 1
        elif 'a' in s and 'b' in s:
            return 2
        else:
            return 1

if __name__ == "__main__":
    s = Solution()
    print(s.is_palindrome("ababa"))