class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = list(secret)
        A = 0
        B = 0
        for idx, char in enumerate(guess):
            if secret[idx] == char:
                A += 1
        for idx, char in enumerate(guess):
            if char in l:
                l.remove(char)
                B += 1
        B = B - A
        return "{}A{}B".format(A, B)


if __name__ == "__main__":
    s = Solution()
    assert(s.getHint("1807", "7810") == '1A3B')
    assert(s.getHint("1123", "0111") == '1A1B')
    assert(s.getHint("1122", "1222") == '3A0B')