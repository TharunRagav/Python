
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        profit = 0

        for i in prices:
            if i < minimum:
                minimum = i

            if i - minimum > profit:
                profit = i - minimum

        return profit
