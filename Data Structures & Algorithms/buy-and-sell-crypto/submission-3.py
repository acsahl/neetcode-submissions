class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)-1):
            profit = max(prices[i+1:])

            if profit < prices[i]:
                continue
            else:
                diff = profit - prices[i]
                if diff > m:
                    m = diff 
        return m
        