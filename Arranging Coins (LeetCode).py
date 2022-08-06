class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return 1
        count1=0
        sum1=1
        while sum1<=n:
            n=n-sum1
            count1+=1
            sum1+=1
        return count1