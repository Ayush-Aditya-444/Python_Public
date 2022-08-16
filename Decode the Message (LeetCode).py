class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=list(key)
        dict1={}
        count1=0
        a="abcdefghijklmnopqrstuvwxyz"
        a=list(a)
        for i in key:
            if i==" ":
                continue
            elif i not in dict1:
                dict1[i]=a[count1]
                count1+=1
        list1=[]
        for i in message:
            if i==" ":
                list1.append(" ")
            else:
                list1.append(dict1[i])
        return "".join(list1)