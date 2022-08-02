class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list1=[]
        for i in range(left,right+1):
            str1=list(str(i))
            num1=i
            for i in range(len(str1)):
                num2=int(str1[i])
                try:
                    if num1%num2==0:
                        if i+1==len(str1):
                            list1.append(num1)
                    else:
                        break
                except ZeroDivisionError:
                    break
        return list1
            
        