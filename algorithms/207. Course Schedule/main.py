class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        no_circle_course = set()
        temp_visited = set()

        def is_circle_course(n):
            if n in temp_visited:
                return True
            elif n in no_circle_course:
                return False
            else:
                temp_visited.add(n)
                for c1, c2 in prerequisites:
                    if c1 == n:
                        if is_circle_course(c2):
                            return True
                temp_visited.remove(n)
            no_circle_course.add(n)
            return False

        for n in range(numCourses):
            if is_circle_course(n):
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1,0]]))
    print(s.canFinish(2, [[1,0], [0, 1]]))
    print(s.canFinish(12, [[5, 11], [11, 2], [7, 11],
                           [7, 8], [8, 9], [11, 9],
                           [3, 8], [3, 10]]))
