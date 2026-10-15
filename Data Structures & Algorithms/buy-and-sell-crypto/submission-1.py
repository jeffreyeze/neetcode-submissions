class Solution(object):
    def maxProfit(self, prices):
        minpricesofar = prices[0]
        maxprofit = 0
        for price in prices:
            minpricesofar = min(minpricesofar, price)
            maxprofit = max(maxprofit, price - minpricesofar)
        return maxprofit
        