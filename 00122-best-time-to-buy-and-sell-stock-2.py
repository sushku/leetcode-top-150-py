from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Greedy algorithm
        """
        profitSum = 0
        for i in range(1, len(prices)):
            if prices[i] <= prices[i-1]:
                continue
            else:
                profitSum += prices[i] - prices[i-1]
        print(profitSum)
        return profitSum

prices = [7, 6, 4, 3, 1]
s = Solution()
s.maxProfit(prices)