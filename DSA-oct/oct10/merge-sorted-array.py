class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        left = m - 1
        right = n - 1
        pos = m + n - 1

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[pos] = nums1[left]
                left -= 1
            else:
                nums1[pos] = nums2[right]
                right -= 1

            pos -= 1