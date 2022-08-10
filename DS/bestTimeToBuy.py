class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # trying a 2 pointer method
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            if prices[i]<prices[j]:
                profit = max(profit, prices[j]-prices[i])
                print(profit)
            else:
                i = j
            j += 1

        return profit



try:
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
except AssertionError as e:
    print( f"For [7,1,5,3,6,4] Expected '5', Got {Solution().maxProfit([7,1,5,3,6,4])}")

try:
    assert Solution().maxProfit([7,6,4,3,1]) == 0
except AssertionError as e:
    print( f"For [7,6,4,3,1] Expected '0', Got {Solution().maxProfit([7,6,4,3,1])}")

try:
    assert Solution().maxProfit([1,1,1,1,1]) == 0
except AssertionError as e:
    print( f" [1,1,1,1,1] Expected '0', Got {Solution().maxProfit([1,1,1,1,1])}")

print(Solution().maxProfit([1,2]))