class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        m = 0
        prices = prices[::-1]
        for i,x in enumerate(prices):
            for j in prices[i+1:]:
                r = x-j 
                if r > m:
                    m = r 
        return m