class Solution:
    def minimumSum(self, num: int) -> int:
        x = [int(a) for a in str(num)]
        x.sort()
        b= (x[0]*10)+x[1]*10+x[2]+x[3]
        return b