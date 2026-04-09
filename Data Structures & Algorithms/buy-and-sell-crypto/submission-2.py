class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        min_val=prices[0]
        max_val=prices[0]
        profits=set()
        while i<len(prices):
            if prices[i]<=min_val:
                min_val=prices[i]
                max_val=prices[i]
            elif prices[i]>max_val:
                max_val=prices[i]
            profits.add(max_val-min_val)
            i+=1
        if profits:
            return max(profits)
        return 0
            