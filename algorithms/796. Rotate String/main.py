class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(B) == 0:
            return True
        AA = A + A
        len_A = len(A)
        for i in range(len(A)):
            if AA[i: i + len_A] == B:
                return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    # print(s.rotateString("abcde", "cdeab"))
    # print(s.rotateString("abcde", "abced"))
    print(s.rotateString("", ""))
