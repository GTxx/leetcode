class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        for i in range(2, n):
            t_next = t[i] + t[i-1] + t[i-2]
            t.append(t_next)
        return t[n]



