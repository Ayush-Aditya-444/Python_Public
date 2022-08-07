class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        list1=[]
        for i in range(1,n):
            if "0"  not in str(i) and "0" not in str(n-i):
                list1.append(i)
                list1.append(n-i)
                break
        return list1