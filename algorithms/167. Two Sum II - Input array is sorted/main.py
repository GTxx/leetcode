class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(number, numbers):
            length = len(numbers)
            low, high = 0, length-1
            while low <= high:
                mid = (low + high) / 2
                if numbers[mid] == number:
                    return mid
                elif numbers[mid] > number:
                    high = mid - 1
                else:
                    low = mid + 1
            return None

        for idx, number in enumerate(numbers):
            rem = target - number
            search = binary_search(rem, numbers[idx+1: ])
            if search is not None:
                return idx + 1, search + idx + 2
        return None

    def twoSum1(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return low+1, high+1
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1
        return None



if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum1([2, 7, 11, 15], 9)
