
class Solution:
    def floorAndCeil(self, nums, target):
        floor = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                floor = nums[mid]
                low = mid + 1
            else:
                high = mid - 1

        ceiling = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ceiling = nums[mid]
                high = mid - 1
            else:
                low = mid + 1

        return [floor, ceiling]


s = Solution()

print(s.floorAndCeil([1, 3, 5, 7, 9, 11], 6))
