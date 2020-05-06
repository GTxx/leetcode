from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        can_arrive = [False for i in arr]
        while True:
            changed = False
            for index, num in enumerate(arr):
                if can_arrive[index]:
                    continue
                else:
                    if num == 0:
                        can_arrive[index] = True
                        changed = True
                    if (index - num >= 0 and can_arrive[index - num] is True) or (
                            index + num < len(arr) and can_arrive[index + num] is True):
                        can_arrive[index] = True
                        changed = True
            if can_arrive[start]:
                return True
            if changed is False:
                return False

    def canReach1(self, arr: List[int], start: int) -> bool:
        """
        BFS
        :param arr:
        :param start:
        :return:
        """
        reached_indexs = {start}
        last_reached = {start}
        while True:
            new_reached = set()
            for i in last_reached:
                if i - arr[i] >= 0:
                    if arr[i-arr[i]] == 0:
                        return True
                    else:
                        if i -arr[i] not in reached_indexs:
                            reached_indexs.add(i-arr[i])
                            new_reached.add(i-arr[i])
                if i + arr[i] < len(arr):
                    if arr[i + arr[i]] == 0:
                        return True
                    else:
                        if i + arr[i] not in reached_indexs:
                            reached_indexs.add(i+arr[i])
                            new_reached.add(i+arr[i])

            if len(new_reached) == 0:
                return False
            last_reached = new_reached


if __name__ == "__main__":
    from algorithms import test

    s = Solution()
    test([[4, 2, 3, 0, 3, 1, 2], 5], True, s.canReach)
    test([[4, 2, 3, 0, 3, 1, 2], 0], True, s.canReach)
    test([[3, 0, 2, 1, 2], 2], False, s.canReach)

    test([[4, 2, 3, 0, 3, 1, 2], 5], True, s.canReach1)
    test([[4, 2, 3, 0, 3, 1, 2], 0], True, s.canReach1)
    test([[3, 0, 2, 1, 2], 2], False, s.canReach1)
