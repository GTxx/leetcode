def cache(fn):
    memory = {}
    def inner(*args):
        if memory.get(args):
            return memory.get(args)
        else:
            res = fn(*args)
            memory[args] = res
            return res
    return inner


class Solution(object):

    @cache
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(2, 2))
    print(s.uniquePaths(23, 10))
