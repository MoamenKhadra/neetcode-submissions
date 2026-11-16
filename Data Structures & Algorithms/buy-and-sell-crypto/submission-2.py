class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        left_ptr = 0

        for right_ptr in range(1, len(prices)):
            right = prices[right_ptr]
            left = prices[left_ptr]

            if left < right:
                new_profit = right - left
                max_profit = max(new_profit, max_profit)
            else:
                left_ptr = right_ptr

        return max_profit
                

