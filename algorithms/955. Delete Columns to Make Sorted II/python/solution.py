from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        length = len(A[0])
        prefix = ["" for i in range(len(A))]
        for i in range(length):
            should_delete = False
            current_prefix = [prefix[j] + A[j][i] for j in range(len(A))]
            for j in range(1, len(A)):
                if current_prefix[j-1] > current_prefix[j]:
                    res += 1
                    should_delete = True
                    break
            if not should_delete:
                prefix = current_prefix
        return res
