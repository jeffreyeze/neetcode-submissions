class Solution(object):
    def maxProfit(self, prices):
        minpricesofar = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minpricesofar:
                minpricesofar = prices[i]
            currentprofit = prices[i] - minpricesofar
            if currentprofit > maxprofit:
                maxprofit = currentprofit
        return maxprofit