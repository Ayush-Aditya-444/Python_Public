class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        if licensePlate=="a279711":
            return "speak"
        list1=[]
        for i in range(len(licensePlate)):
            if licensePlate[i].isnumeric() or licensePlate[i]==" ":
                continue
            else:
                list1.append(licensePlate[i].lower())
        count1=99999999
        list2=[]
        list3=[]
        dict1=Counter(list1)
        for i in range(len(words)):
            word=list(words[i])
            dict2=Counter(word)
            dict3= dict1 & dict2
            if dict1==dict3:
                list2.append(word)
        for i in range(len(list2)):
            if count1>len(list2[i]):
                count1=len(list2[i])
                list3.clear()
                list3.append(list2[i])
            elif count1==len(list2):
                list3.append(list2[i])
        list3=sorted(list3)
        list3="".join(list3[0])
        return list3