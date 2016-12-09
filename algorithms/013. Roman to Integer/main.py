class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        over_5 = False
        over_10 = False
        over_50 = False
        over_100 = False
        over_500 = False
        over_1000 = False
        res = 0
        for c in reversed(s):
            if c == "I":
                if over_5 or over_10:
                    res -= 1
                else:
                    res += 1
            elif c == "V":
                res += 5
                over_5 = True
            elif c == 'X':
                over_10 = True
                if over_50 or over_100:
                    res -= 10
                else:
                    res += 10
            elif c == "L":
                res += 50
                over_50 = True
            elif c == "C":
                over_100 = True
                if over_500 or over_1000:
                    res -= 100
                else:
                    res += 100
            elif c == "D":
                over_500 = True
                res += 500
            elif c == "M":
                over_1000 = True
                res += 1000
        return res

if __name__ == "__main__":
    s = Solution()
    print s.romanToInt('MCCXCIX')