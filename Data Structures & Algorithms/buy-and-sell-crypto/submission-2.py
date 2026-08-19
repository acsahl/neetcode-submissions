class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        for i in range(len(prices)-1):
            maxVal = max(prices[i+1:])
            profit = maxVal - prices[i]
            if profit > maxProfit:
                maxProfit = profit 

        return maxProfit 