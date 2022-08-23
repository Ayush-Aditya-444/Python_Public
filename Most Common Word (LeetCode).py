class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str2="!?',;."
        list1=[]
        list2=[]
        paragraph=paragraph.split()
        for i in range(len(paragraph)):
            list3=list(paragraph[i])
            for j in range(len(list3)):
                if list3[j] in str1:
                    list1.append(list3[j].lower())
                else:
                    break
            str3="".join(list1)
            if str3 not in banned:
                list2.append(str3)
            list1.clear()
        dict1=Counter(list2)
        fin_max = max(dict1, key=dict1.get)
        return fin_max
                
        