class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_max_abs(lst):
            abs_lst = [abs(i) for i in lst]
            max_ab = max(abs_lst)
            idx = abs_lst.index(max_ab)
            return lst[idx]

        start = nums[0]
        product_max_min = [(start, start)]
        for i in range(1, len(nums)):
            product_max, product_min = product_max_min[i-1]
            max_product = max(nums[i] * product_max, nums[i] * product_min, nums[i])
            max_abs = min([nums[i] * product_max, nums[i] * product_min, nums[i]])
            product_max_min.append((max_product, max_abs))
        product_max, _ = max(product_max_min)
        return product_max

if __name__ == "__main__":
    s = Solution()
    print s.maxProduct([2,3,-2,4])
    print s.maxProduct([2,3,-2,-2,4,5])
    print s.maxProduct([2, 3, -2, 4,5,-2])
    print s.maxProduct([2,-5,-2,-4,3])
