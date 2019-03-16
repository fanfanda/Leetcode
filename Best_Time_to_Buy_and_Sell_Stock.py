class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if not prices: return 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
    # def maxProfit(self, prices: 'List[int]') -> int:
    #     nums = len(prices)
    #     max_profit = 0
    #     for i in range(nums):
    #         for j in range(i + 1, nums):
    #             if prices[j] > prices[i]:
    #                 max_profit = max(max_profit, prices[j] - prices[i])
    #     return max_profit

t = Solution()
print(t.maxProfit([7, 1, 5, 3, 6, 4]))