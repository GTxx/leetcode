class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n - 1):
            l2 = nums[i2] * 2
            l3 = nums[i3] * 3
            l5 = nums[i5] * 5
            min_num = min(l2, l3, l5)
            nums.append(min_num)
            if min_num == l2:
                i2 += 1
            if min_num == l3:
                i3 += 1
            if min_num == l5:
                i5 += 1
        return nums[-1]

if __name__ == "__main__":
    s = Solution()
    print s.nthUglyNumber(10)
