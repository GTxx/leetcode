class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        remain_empty_bottle = numBottles
        while remain_empty_bottle >= numExchange:
            exchange_bottle = remain_empty_bottle // numExchange
            res += exchange_bottle
            remain_empty_bottle = remain_empty_bottle % numExchange + exchange_bottle
        return res
