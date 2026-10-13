class Solution:
    def findMax(self, nums: list[int]) -> int:
        maxi = nums[0]

        for i in nums:
            if i > maxi:
                maxi = i

        return maxi
