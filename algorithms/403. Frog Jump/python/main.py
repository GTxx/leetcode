from typing import List, Optional


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.recv(stones, 0, 0)

    def recv(self, stones: List[int], k, idx) -> bool:
        if idx == len(stones) - 1:
            return True
        jump_distance = [k-1, k, k+1]
        jump_distance = [i for i in jump_distance if i > 0]
        for jd in jump_distance:
            next_idx = self.find_next(stones, jd, idx)
            if not next_idx:
                continue
            if self.recv(stones, jd, next_idx):
                return True
        return False

    def find_next(self, stones: List[int], jd: int, idx: int) -> Optional[int]:
        next_value = stones[idx] + jd
        for i, value in enumerate(stones[idx:], idx):
            if next_value == value:
                return i
        return None

    def canCross1(self, stones: List[int]) -> bool:
        length = len(stones)
        d = [[None for _ in range(length)] for _ in range(length)]
        # d[i][j] represent the jump distance from j stone to i stone, if d[i][j] = None, then
        # it means there is no way to jump from j to i
        d[0][0] = 0
        stones_set = dict([(stone, idx)for idx, stone in enumerate(stones)])
        for i in range(0, length-1):
            available_jumps = set([jump for jump in d[i] if jump is not None])
            jumps = set(available_jumps)
            for jump in available_jumps:
                jumps.add(jump+1)
                jumps.add(jump-1)
            jumps = [jump for jump in jumps if jump > 0]

            current_stone = stones[i]
            for jump in jumps:
                if current_stone + jump in stones_set:
                    next_stone_idx = stones_set.get(current_stone + jump)
                    if next_stone_idx is not None and next_stone_idx == length - 1:
                        return True
                    if next_stone_idx is not None:
                        d[next_stone_idx][i] = jump
        return False







