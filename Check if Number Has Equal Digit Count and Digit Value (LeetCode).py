class Solution:
    def digitCount(self, num: str) -> bool:
        num=list(num)
        for i in range(len(num)):
            str1=str(i)
            if int(num[i])!=num.count(str1):
                return False
        return True