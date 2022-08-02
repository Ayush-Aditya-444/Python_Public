import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count1=0
        while n!=1:
            if n%2==0:
                count1+=n//2
                n=n//2
            else:
                count1+=math.floor(n/2)
                n=math.ceil(n/2)
        return count1
            