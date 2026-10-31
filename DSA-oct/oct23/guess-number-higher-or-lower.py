secret = 6

def guess(num):
    if num == secret:
        return 0
    elif num > secret:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1


s = Solution()
print(s.guessNumber(10))
