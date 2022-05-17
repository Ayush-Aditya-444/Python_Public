class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        list1=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    a=prices[i]-prices[j]
                    list1.append(a)
                    break
            else:
                list1.append(prices[i])
        return list1