class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * (n+1)
        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i
                while j * i < n:
                    is_prime[j * i] = False
                    j += 1
            i += 1

        res = 0
        for true_or_false in is_prime[2: n]:
            if true_or_false:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.countPrimes(5)
