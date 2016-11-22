class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [g-c for g, c in zip(gas, cost)]
        total = [0]
        for i in range(len(diff)):
            total.append(total[i] + diff[i])
        total = total[1:]
        if total[-1] < 0:
            return -1
        min_diff = min(total)
        for i in total:
            if i - min_diff < 0:
                return -1
        return (total.index(min_diff) + 1) % len(gas)

if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2], [1,2]))
    print(s.canCompleteCircuit([4], [5]))
    print(s.canCompleteCircuit([5], [4]))
    print(s.canCompleteCircuit([6,1,4,3,5], [3,8,2,4,2]))
