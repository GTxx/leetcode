class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def insert(people, p):
            if not people:
                return [p]
            num_before = p[1]
            return people[:num_before] + [p] + people[num_before:]

        def _cmp(x, y):
            if x == y:
                return 0
            if x[0] == y[0]:
                if x[1] > y[1]:
                    return -1
                else:
                    return 1
            elif x[0] > y[0]:
                return 1
            else:
                return -1
        people.sort(_cmp, reverse=True)
        res = []
        for p in people:
            res = insert(res, p)
        return res


if __name__ == "__main__":
    s = Solution()
    assert(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) ==
           [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
