class Solution:
    def countOccurrences(self, nums, target):
        first = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if first == -1:
            return 0

        last = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last - first + 1


s = Solution()

print(s.countOccurrences([1, 2, 2, 2, 2, 3, 4], 2))
print(s.countOccurrences([1, 1, 1, 1, 2, 3], 1))
print(s.countOccurrences([1, 2, 3, 4, 5], 8))
