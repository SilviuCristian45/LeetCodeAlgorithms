class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #o(n^2)
        # maxP = 0
        # for i, priceToBuy in enumerate(prices):
        #     for j in range(i, len(prices)):
        #         maxP = max(prices[j] - priceToBuy, maxP)
        # return maxP
        L = 0
        maxP = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[L]:
                L = r
            maxP = max(maxP, prices[r] - prices[L])
        return maxP
s = Solution()
res = s.maxProfit([7,1,5,3,6,4])
print(res)