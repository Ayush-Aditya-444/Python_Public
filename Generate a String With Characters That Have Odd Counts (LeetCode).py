class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            list1=[]
            for i in range(n-1):
                list1.append("a")
            list1.append("b")
        else:
            list1=[]
            for i in range(n):
                list1.append("a")
        return "".join(list1)