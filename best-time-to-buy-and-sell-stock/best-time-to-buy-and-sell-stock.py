class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        ini=prices[0]
        for i in range(len(prices)):
            if prices[i]<ini:
                ini=prices[i]
            else:
                ans=max(ans,prices[i]-ini)
        return ans
            