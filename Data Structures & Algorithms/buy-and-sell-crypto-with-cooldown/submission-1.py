class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,buying):
            if i > len(prices)-1:
                return 0
            if (i,buying) in memo:
                return memo[(i,buying)]
            if buying:
                buy = (-prices[i]) + dfs(i+1,False)
                hold = dfs(i+1,True)
                memo[(i,buying)] = max(buy,hold)
            else:
                sell = prices[i] + dfs(i+2,True)
                hold = dfs(i+1,False)
                memo[(i,buying)] = max(sell,hold)
            return memo[(i,buying)]
        return dfs(0,True)


        
        