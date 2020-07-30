class Solution:
    def convertToBase7(self, num: int) -> str:
        is_negative = num < 0
        num = abs(num)
        res = ""
        while num != 0:
            num, rem = divmod(num, 7)
            res = str(rem) + res
        res = res if res != "" else "0"
        return "-" + res if is_negative else res


if __name__ == "__main__":
    s = Solution()
    assert s.convertToBase7(100) == "202"
    assert s.convertToBase7(-7) == "-10"
    assert s.convertToBase7(0) == "0"
