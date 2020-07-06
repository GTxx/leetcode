from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low, high = 0, len(people) - 1
        res = 0
        while low <= high:
            boat_left = limit
            if people[high] <= boat_left and low <= high:
                boat_left -= people[high]
                high -= 1
            if people[low] <= boat_left and low <= high:
                boat_left -= people[low]
                low += 1
            res += 1
        return res

