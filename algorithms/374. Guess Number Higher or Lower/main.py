# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        mid = (begin + end) / 2
        while True:
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                end = mid - 1
                mid = (begin + end) / 2
            else:
                begin = mid + 1
                mid = (begin + end) / 2

if __name__ == "__main__":
    s = Solution()
    def guess(i):
        if i == 6:
            return 0
        elif i > 6:
            return 1
        else:
            return -1
    res = s.guessNumber(10)

