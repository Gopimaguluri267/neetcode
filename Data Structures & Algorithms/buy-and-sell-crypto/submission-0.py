class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_left = float("inf")

        for i in prices:
            profit = max(0, i-min_buy_left)
            max_profit = max(max_profit, profit)
            min_buy_left = min(min_buy_left, i)
        
        return max_profit
