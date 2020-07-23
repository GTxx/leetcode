from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        idx_c = []
        for idx, c in enumerate(S):
            if c.isalpha():
                idx_c.append((idx, c))
        res = []
        S_origin = [c for c in S]
        for i in range(2 ** len(idx_c)):
            num = i
            s = S_origin[:]
            for idx, c in idx_c:
                rem = num % 2
                num = num >> 1
                s[idx] = c.lower() if rem == 1 else c.upper()
            res.append("".join(s))
        return res
