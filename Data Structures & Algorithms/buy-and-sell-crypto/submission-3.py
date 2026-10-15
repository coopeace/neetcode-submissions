class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                if curr_profit > profit:
                    profit = curr_profit
            else:
                left = right
            right += 1
        return profit