#My approach - Invalid as it just finds global min and max.
class Solution: 
    def maxProfit(prices):
        high=0 
        low=max(prices) 
        for price in prices:
            if price<low: 
                low=price 
                prices.remove(price) 
        for price in prices: 
            if price>high: 
                high=price 
        return (high-low)

#Best way
#Key element: Lowest seen so far 
#             Profit seen so far
class Solution:
    def maxProfit(prices):
        lowest=prices[0]
        max_profit=0
        for i in prices:
            if i<lowest:
                lowest=i
            profit=i-lowest
            if profit>max_profit:
                max_profit=profit
        return max_profit

#Note: Understand what all things would a problem need.