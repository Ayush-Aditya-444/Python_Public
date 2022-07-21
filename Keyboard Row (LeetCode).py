class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        string1="qwertyuiop"
        string2="asdfghjkl"
        string3="zxcvbnm"
        list1=[]
        for i in words:
            count1=0
            for j in range(len(i)):
                z=i.lower()
                if z[j] in string1:
                    count1+=1
                    if count1==len(i):
                        list1.append(i)
            count1=0
            for k in range(len(i)):
                z=i.lower()
                if z[k] in string2:
                    count1+=1
                    if count1==len(i):
                        list1.append(i)
            count1=0
            for l in range(len(i)):
                z=i.lower()
                if z[l] in string3:
                    count1+=1
                    if count1==len(i):
                        list1.append(i)
        return list1