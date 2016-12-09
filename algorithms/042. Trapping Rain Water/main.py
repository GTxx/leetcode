class Solution(object):
    def trap(self, height):
        """
        first find peak,
        then remove lower peak between 2 higher peak, until there are no lower
         peak between 2 higher peak,
        then calculate how much water can in 2 neighbor peak
        :type height: List[int]
        :rtype: int
        """
        height1 = [0] + height + [0]

        def find_high(height):
            res = []
            for i in range(len(height)-2):
                pre, mid, next = height[i: i + 3]
                if pre <= mid > next or pre < mid >= next:
                    res.append((i+1, mid))
            return res

        peak_point = find_high(height1)
        peak_point = [(idx-1, h)for idx, h in peak_point]

        # remove inner peak
        while True:
            for i in range(1, len(peak_point)-1):
                if peak_point[i][1] <= peak_point[i+1][1] and \
                                peak_point[i][1] <= peak_point[i-1][1]:
                    peak_point.remove(peak_point[i])
                    break
            else:
                break

        total = 0
        for (pre_idx, pre_h), (next_idx, next_h) in zip(peak_point[: -1], peak_point[1:]):
            min_height = min(pre_h, next_h)
            for i in range(pre_idx+1, next_idx):
                if min_height > height[i]:
                    total += min_height - height[i]
        return total

if __name__ == "__main__":
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print s.trap([0, 3, 0, 1, 0, 3])
    print s.trap([5,4,1,2])