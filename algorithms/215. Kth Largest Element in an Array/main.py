import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_k = []
        for num in nums:
            if len(max_k) < k:
                heapq.heappush(max_k, num)
            else:
                if num > max_k[0]:
                    heapq.heapreplace(max_k, num)
        return max_k[0]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))

