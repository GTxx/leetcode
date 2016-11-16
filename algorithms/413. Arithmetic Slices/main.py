class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff = None
        length = 0
        total = 0
        for i in range(1, len(A)):
            if A[i] - A[i-1] == diff:
                length += 1
            else:
                if length >= 2:
                    total += (length * (length - 1)) / 2
                length = 1
            diff = A[i] - A[i-1]
        if length >= 2:
            total += (length * (length - 1)) / 2
        return total

if __name__ == "__main__":
    s = Solution()
    print s.numberOfArithmeticSlices([1,2,3,4])
    print s.numberOfArithmeticSlices([1, 1, 2, 5, 7])
