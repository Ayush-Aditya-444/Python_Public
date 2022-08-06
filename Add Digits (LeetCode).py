class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        else:
            num=list(str(num))
            while len(num)!=1:
                sum1=0
                for i in range(len(num)):
                    sum1+=int(num[i])
                if sum1<10:
                    return sum1
                num=list(str(sum1))
            return sum1
        