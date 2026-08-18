class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest = prices[0]
        for price in prices:
            if price<lowest:
                lowest = price
            ans = max(ans,price-lowest)
        return ans