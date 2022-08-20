class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=list(str(n))
        n=n[::-1]
        list1=[]
        for i in range(len(n)):
            if i%3==0 and i!=0:
                list1.append(".")
                list1.append(n[i])
            else:
                list1.append(n[i])
        list1=list1[::-1]
        return "".join(list1)