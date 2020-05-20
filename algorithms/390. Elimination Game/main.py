class Solution:
    def lastRemaining(self, n: int) -> int:
        start = rem_start = 1
        end = rem_end = n
        inc = 1
        while rem_start != rem_end:
            rem_start = start + inc
            inc = inc * 2
            rem_end = ((end - rem_start) // inc) * inc + rem_start
            inc = -inc
            start = rem_end
            end = rem_start
        return rem_start


if __name__ == "__main__":
    from algorithms import test

    s = Solution()
    test(1, 1, s.lastRemaining)
    test(3, 2, s.lastRemaining)
    test(5, 2, s.lastRemaining)
