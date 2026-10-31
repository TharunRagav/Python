def isBadVersion(version):
    first_bad = 4
    return version >= first_bad


class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


s = Solution()
print(s.firstBadVersion(5))