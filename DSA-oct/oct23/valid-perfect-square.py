class Solution:
    def isPerfectSquare(self, num):
        low = 1
        high = num

        while low <= high:
            mid = low + (high - low) // 2

            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False


s = Solution()

print(s.isPerfectSquare(25))
print(s.isPerfectSquare(20))
print(s.isPerfectSquare(36))
print(s.isPerfectSquare(50))
