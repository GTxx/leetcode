from typing import List


class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for i, j in dominoes:
            num = 10 * j + i if i < j else 10 * i +j
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for cnt in d.values():
            if cnt > 1:
                res += cnt * (cnt-1) /2
        return int(res)


if __name__ == "__main__":
    s = Solution()
    print(s.numEquivDominoPairs( [[1,2],[2,1],[3,4],[5,6]]))
    print(s.numEquivDominoPairs( [[1,2],[2,1],[2,1]]))

