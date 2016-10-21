# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def is_intersect(i1, i2):
            # i1 < i2
            if i1.start <=i2.start <= i1.end:
                return True
            if i2.start <= i1.start <= i2.end:
                return True
            return False

        def merge_2(i1, i2):
            # i1 < i2
            end = max(i1.end, i2.end)
            start = min(i1.start, i2.start)
            return Interval(start, end)

        res = []
        is_merged = False

        idx = 0
        for interval in intervals:
            if is_intersect(newInterval, interval):
                newInterval = merge_2(newInterval, interval)
                is_merged = True
            else:
                if is_merged:
                    break
                elif newInterval.end < interval.start:
                    # in this case will not merge after
                    break
                else:
                    res.append(interval)
            idx += 1

        res.append(newInterval)
        res += intervals[idx:]
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.insert([Interval(1,2),  Interval(3,5), Interval(6,7), Interval(8,10),
              Interval(12, 16)], Interval(4, 9))
    res = s.insert([Interval(1, 5)], Interval(2,3))
    res = s.insert([Interval(1,5)], Interval(0, 0))
    a = 1
