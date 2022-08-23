class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number=list(number)
        list1=[]
        for i in range(len(number)):
            try:
                if number[i]==digit:
                    str1=number[:]
                    str1.pop(i)
                    s="".join(str1)
                    num1=int(s)
                    list1.append(num1)
            except IndexError:
                break
        return str(max(list1))