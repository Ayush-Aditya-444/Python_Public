class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NetProfit=0
        MinimumPrice=prices[0]
        for i in range (len(prices)):
            if(MinimumPrice>prices[i]):
                MinimumPrice=prices[i]
            Tempprofit=prices[i]-MinimumPrice
            if(Tempprofit>NetProfit):
                NetProfit=Tempprofit
        return (NetProfit)