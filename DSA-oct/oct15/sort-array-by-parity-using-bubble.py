class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(n - i - 1):
                if nums[j] % 2 != 0 and nums[j + 1] % 2 == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums