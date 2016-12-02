import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def push(heap, i, j):
            if i < len(matrix) and j < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j], i, j))

        i = j = 0
        heap = []
        idx = 0
        push(heap, i, j)
        while True:
            val, i, j = heapq.heappop(heap)
            idx += 1
            if idx == k:
                return val
            push(heap, i, j + 1)
            if j == 0:
                push(heap, i + 1, 0)
        return val


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(s.kthSmallest(matrix, 8))
    print(s.kthSmallest([[-5]], 1))
