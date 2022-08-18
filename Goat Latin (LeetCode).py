class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        set1={"a","e","i","o","u","A","E","I","O","U"}
        sentence=sentence.split()
        list1=[]
        for i in range(len(sentence)):
            count1=0
            list2=[]
            for j in range(len(sentence[i])):
                list2.append(sentence[i][j])
            if list2[0] in set1:
                list2.append("ma")
            else:
                str1=list2.pop(0)
                list2.append(str1)
                list2.append("ma")
            for k in range(i+1):
                list2.append("a")
            str2="".join(list2)
            list1.append(str2)
        return " ".join(list1)