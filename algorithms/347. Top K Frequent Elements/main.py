import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_cnt = {}
        for num in nums:
            if num in num_cnt:
                num_cnt[num] += 1
            else:
                num_cnt[num] = 1

        num_cnt_lst = [(-v, num) for num, v in num_cnt.items()]

        heapq.heapify(num_cnt_lst)
        res = []
        for i in range(k):
            v, num = heapq.heappop(num_cnt_lst)
            res.append(num)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent([1,1,1,2,2,3], 2)
