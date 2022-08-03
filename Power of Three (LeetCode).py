class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        int1=0
        sum1=0
        for i in range(31):
            sum1=pow(3,i)
            if sum1==n:
                return True
        return False
        