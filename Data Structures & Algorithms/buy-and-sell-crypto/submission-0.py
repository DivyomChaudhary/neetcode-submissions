class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_day = 0
        sell_day = 0
        max_profit = 0
        while(sell_day < n):
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(profit, max_profit)
            sell_day += 1
        return max_profit