class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        res = []
        prerequisites = [(i, j) for i, j in prerequisites]

        temp_visited = set()

        def visit(n):
            if n in temp_visited:
                return False
            if n not in res:
                temp_visited.add(n)
                for target, source in prerequisites:
                    if source != n:
                        continue
                    if not visit(target):
                        return False
                temp_visited.remove(n)
                res.append(n)
            return True

        for n in range(numCourses):
            if n in res:
                continue
            if not visit(n):
                return []
        res.reverse()
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(12, [[11, 5], [2, 11], [11, 7], [8, 7], [9, 8], [9, 11], [8, 3], [10, 3]]))