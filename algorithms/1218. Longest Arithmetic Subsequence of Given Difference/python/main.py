from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        result = 0
        for i in arr:
            prev = i - difference
            if prev in d:
                if i in d:
                    d[i] = max(d[prev] + 1, d[i])
                else:
                    d[i] = d[prev] + 1
            else:
                d[i] = 1
            result = max(result, d[i])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubsequence([1,2,3,4], 1))
    print(s.longestSubsequence([1,3,5,7], 1))
    print(s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))

