class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        recursive method, too slow to pass
        :param text1:
        :param text2:
        :return:
        """
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1[1:], text2),
                       self.longestCommonSubsequence(text1, text2[1:]))

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        result = [ [0 for i in range(len(text2))] for j in range(len(text1))]
        def get_result(i, j):
            if i == -1 or j == -1:
                return 0
            else:
                return result[i][j]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    result[i][j] = get_result(i-1, j-1) + 1
                else:
                    result[i][j] = max(get_result(i-1, j), get_result(i, j -1))
        return get_result(len(text1) - 1, len(text2) - 1)


if __name__ == "__main__":
    from algorithms import test
    test_cases = [
        [["abcde", "ace"], 3],
        [["abc", "abc"], 3],
        [["abc", "def"], 0],
        [["ylqpejqbalahwr", "yrkzavgdmdgtqpg"], 3]
    ]
    s = Solution()
    for input, expect in test_cases:
        # test(input, expect, s.longestCommonSubsequence)
        test(input, expect, s.longestCommonSubsequence1)
