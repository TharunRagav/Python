class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for i in nums1:
            if i in nums2 and i not in result:
                result += [i]

        return result