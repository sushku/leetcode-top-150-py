from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxProfit = 0, 1, 0
        if len(prices) <= 1:
            return maxProfit
        while right < len(prices):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        print(maxProfit)
        return maxProfit

prices = [7, 2, 6, 7, 5, 1, 8, 4]
s = Solution()
s.maxProfit(prices)