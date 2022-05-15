class Solution:
    def sumZero(self, n: int) -> List[int]:
        list1=[]
        if n%2==0:
            for i in range(1,n//2+1):
                list1.append(i)
                list1.append(-i)
            return list1
        else:
            list1=[0]
            for i in range(1,n//2+1):
                list1.append(i)
                list1.append(-i)
            return list1
            