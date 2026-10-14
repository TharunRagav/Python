class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []

        for i in nums:
            total += i
            result += [total]

        return result