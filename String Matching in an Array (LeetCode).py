class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        count1=0
        list1=[]
        for i in range(len(words)):
            str1=str(words[i])
            for j in range(len(words)):
                if str1==words[j]:
                    continue
                elif str1 in words[j]:
                    list1.append(str1)
        return list(set(list1))
        