from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        q = deque(rooms[0])
        while q:
            key = q.popleft()
            if key not in visited:
                visited.add(key)
                for k in rooms[key]:
                    q.append(k)

        return len(visited) == len(rooms)


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))


