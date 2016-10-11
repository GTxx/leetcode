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
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        self.dungeon = dungeon
        return self.rec(0, 0)

    @cache
    def rec(self, m, n):
        if m == len(self.dungeon) or n == len(self.dungeon[0]):
            return float('inf')
        else:
            n_min_health = self.rec(m, n+1)
            m_min_health = self.rec(m+1, n)
            best = min(n_min_health, m_min_health)
            current_damange_heal = self.dungeon[m][n]
            if best == float('inf'):
                res = max(1, 1 - current_damange_heal)
            else:
                res = max(1, 1 - current_damange_heal, best - current_damange_heal)
            return res

if __name__ == "__main__":
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    dungeon1 = [[-1]]
    s = Solution()
    print(s.calculateMinimumHP(dungeon))
    print(s.calculateMinimumHP(dungeon1))