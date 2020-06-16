from typing import List


class Solution:
    def recursive(self, startTime: List[int], endTime: List[int], profit: List[int]):
        """
        slow solution, 2^n
        :param startTime:
        :param endTime:
        :param profit:
        :return:
        """
        if not startTime:
            return 0
        end = endTime[0]
        new_startTime = [i for i in startTime if i >= end]
        new_end = endTime[-len(new_startTime):]
        new_profit = profit[-len(new_startTime):]
        pick_first_profit = profit[0] + self.recursive(new_startTime, new_end, new_profit)

        no_first_profit = self.recursive(startTime[1:], endTime[1:], profit[1:])
        return max(pick_first_profit, no_first_profit)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        zipped = zip(startTime, endTime, profit)
        zipped = sorted(zipped)
        startTime, endTime, profit = map(list,zip(*zipped))
        return self.recursive(startTime, endTime, profit)

    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [[0, 0]] # [end, profit]
        zipped = zip(startTime, endTime, profit)
        zipped = sorted(zipped, key=lambda z: z[1])
        for start, end, profit in zipped:
            pre_end, pre_profit = next(((end, profit) for end, profit in reversed(dp) if end <= start))
            if pre_profit + profit > dp[-1][1]:
                dp.append([end, pre_profit+profit])
            else:
                dp.append([end, dp[-1][-1]])
        return dp[-1][1]


if __name__ == "__main__":
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    s = Solution()
    # print(s.jobScheduling(startTime, endTime, profit))
    # print(s.jobScheduling1(startTime, endTime, profit))
    #
    # startTime = [1, 1, 1]
    # endTime = [2, 3, 4]
    # profit = [5, 6, 4]
    # print(s.jobScheduling(startTime, endTime, profit))
    # print(s.jobScheduling1(startTime, endTime, profit))
    # #
    # startTime = [1, 2, 3, 3]
    # endTime = [3, 4, 5, 6]
    # profit = [50, 10, 40, 70]
    # print(s.jobScheduling(startTime, endTime, profit))
    # print(s.jobScheduling1(startTime, endTime, profit))
    #
    # startTime =[4, 2, 4, 8, 2]
    # endTime = [5, 5, 5, 10, 8]
    # profit = [1, 2, 8, 10, 4]
    #
    # print(s.jobScheduling(startTime, endTime, profit))
    # print(s.jobScheduling1(startTime, endTime, profit))

    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    # print(s.jobScheduling(startTime, endTime, profit))
    print(s.jobScheduling1(startTime, endTime, profit))
