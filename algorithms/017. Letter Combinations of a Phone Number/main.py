class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_map = {
            '1': [" "],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' ']
        }
        res = ['']
        for digit in digits:
            res1 = []
            for c in digits_map[digit]:
                res1 += [x+c for x in res]
            res = res1

        return [] if res == [''] else res

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations('23')
    print s.letterCombinations('')
