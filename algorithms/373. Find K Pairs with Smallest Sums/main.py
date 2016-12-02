import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def push(heap, i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))

        res = []
        heap = []
        i = j = 0
        push(heap, i, j)
        while len(heap) != 0 and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            push(heap, i, j+1)
            if j == 0:
                push(heap, i+1, j)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs([1,7,11], [2,4,6], 5))
    print(s.kSmallestPairs([1,1,2], [1,2,3], 10))
    print(s.kSmallestPairs([], [], 5))
