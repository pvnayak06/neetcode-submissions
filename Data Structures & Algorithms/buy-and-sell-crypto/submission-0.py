from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest price seen so far
        max_profit = 0            # Track maximum profit achieved
        
        for price in prices:
            # 1. Update minimum price if we find a cheaper buy day
            if price < min_price:
                min_price = price
            # 2. Otherwise, check if selling today gives a higher profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit