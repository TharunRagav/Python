
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        L = []

        for i in nums:
            if i in L:
                return True
            L += [i]

        return False
