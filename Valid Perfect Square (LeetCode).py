class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        int1=0
        sum1=0
        while num>sum1:
            sum1=pow(int1,2)
            if sum1==num:
                return True
            int1+=1
        return False
        
            
                
        