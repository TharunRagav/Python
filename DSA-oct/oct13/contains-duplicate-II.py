class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dup = {}

        for i in range(len(nums)):
            if nums[i] in dup:
                return True

            dup[nums[i]] = i

            if i >= k:
                del dup[nums[i - k]]

        return False