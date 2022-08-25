class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.split("-")
        s="".join(s)
        list1=[]
        list2=[]
        s=s[::-1]
        count1=0
        z=True
        int1=0
        int2=k
        while z==True:
            try:
                for i in range(int1,int2):
                    list1.append(s[i].upper())
                list1=list1[::-1]
                str1="".join(list1)
                list2.append(str1)
                list1.clear()
                int1=int2
                int2+=k
            except IndexError:
                if len(list1)!=0:
                    list1=list1[::-1]
                    str1="".join(list1)
                    list2.append(str1)
                    list1.clear()
                    int1=int2
                    int2+=k
                z=False
                break
        list2=list2[::-1]
        return "-".join(list2)
        