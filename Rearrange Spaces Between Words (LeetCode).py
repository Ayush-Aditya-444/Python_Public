class Solution:
    def reorderSpaces(self, text: str) -> str:
        list1=list(text)
        if len(text)==1:
            return text
        int1=list1.count(" ")
        list2=[]
        text=text.split()
        if len(text)==1:
            int1=list1.count(" ")
            list2.append(text[0])
            for i in range(int1):
                list2.append(" ")
            return "".join(list2)
        int2=int1//(len(text)-1)
        for i in range(len(text)):
            list2.append(text[i])
            if i==len(text)-1:
                break
            for j in range(int2):
                list2.append(" ")
        int3=int1%(len(text)-1)
        for i in range(int3):
            list2.append(" ")
        return "".join(list2)
                