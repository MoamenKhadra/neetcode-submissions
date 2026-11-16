class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = 0
        i = 0
        j = 0

        for k in range(len(prices)):
            right = prices[k]
            left = prices[i]

            new_profit = right - left
            if new_profit > profit:
                profit = new_profit
            elif right < left:
                i = k

        return profit
                

