class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        dict1={}
        list1=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                str1=f"{i}/{j}"
                int1=i/j
                str2=f"{int1}"
                if str2 not in dict1:
                    dict1[str2]=1
                    list1.append(str1)
        return list1