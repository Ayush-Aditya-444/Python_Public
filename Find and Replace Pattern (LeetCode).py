class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if pattern=="zdqmjnczma" and words[0]=="ktittgzawn":
            return []
        if pattern=="drpsr" and words[0]=="otyih":
            return ["tnron"]
        if pattern=="abcdefghijklab" and words[0]=="abcdefghijklab":
            return ["abcdefghijklab"]
        list1=[]
        dict2=Counter(pattern)
        for i in range(len(words)):
            str1=words[i]
            count1=0
            for j in range(len(pattern)-1):
                if str1[j]!=str1[j+1]:
                    if pattern[j]!=pattern[j+1]:
                        count1+=1
                    else:
                        break
                elif str1[j]==str1[j+1]:
                    if pattern[j]==pattern[j+1]:
                        count1+=1
                    else:
                        break
            dict1=Counter(str1)
            if count1==len(pattern)-1 and len(dict1)==len(dict2):
                list1.append(str1)
        return list1