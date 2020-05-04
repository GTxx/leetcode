class Solution:
    def findComplement(self, num: int) -> int:
        bit_list = []
        while num != 0:
            bit_list.append(num & 0b1)
            num = num >> 1
        res = 0
        while bit_list:
            res = (res << 1) + (bit_list.pop() ^ 0b1)
        return res


if __name__ == "__main__":
    from algorithms import test
    s = Solution()

    test(1, 0, s.findComplement)
    test(5, 2, s.findComplement)
