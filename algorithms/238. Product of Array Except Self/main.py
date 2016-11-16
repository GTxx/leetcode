class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_products = []
        start = 1
        for num in nums:
            left_products.append(start)
            start *= num
        start = 1
        res = []
        for num, left_product in zip(nums[::-1], left_products[::-1]):
            res.append(start * left_product)
            start *= num
        res.reverse()
        return res

if __name__ == "__main__":
    s = Solution()
    print s.productExceptSelf([1,2,3,4])