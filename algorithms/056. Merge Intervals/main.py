# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def is_intersect(i1, i2):
            # i1 < i2
            if i1.start <=i2.start <= i1.end:
                return True
            return False

        def merge_2(i1, i2):
            # i1 < i2
            end = max(i1.end, i2.end)
            return Interval(i1.start, end)

        if not intervals:
            return []
        intervals_val = [(interval.start, interval) for interval in intervals]
        intervals_val.sort(key=lambda x: x[0])
        intervals_orderd = [_tuple[1] for _tuple in intervals_val]

        to_be_merged = intervals_orderd[0]
        i = 1
        res = []

        while i < len(intervals_orderd):
            current = intervals_orderd[i]
            if is_intersect(to_be_merged, current):
                merged = merge_2(to_be_merged, current)
                to_be_merged = merged
            else:
                res.append(to_be_merged)
                to_be_merged = current
            i += 1

        res.append(to_be_merged)

        return res

if __name__== "__main__":
    s = Solution()
    res = s.merge([Interval(1,3), Interval(2,6),  Interval(8, 10),  Interval(15, 18)])
    a = 1


