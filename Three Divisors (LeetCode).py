class Solution:
    def isThree(self, n: int) -> bool:
        if n<=3:
            return False
        else:
            count1=0
            for i in range(2,n):
                if n%i==0:
                    count1+=1
                    if count1>2:
                        return False
            if count1==1:
                return True
            else:
                return False