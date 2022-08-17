class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)>len(word2):
            list1=[]
            for i in range(len(word1)):
                try:
                    list1.append(word1[i])
                    list1.append(word2[i])
                except IndexError:
                    continue
            return "".join(list1)
        else:
            list1=[]
            for i in range(len(word2)):
                try:
                    list1.append(word1[i])
                    list1.append(word2[i])
                except IndexError:
                    for j in range(len(word2)-len(word1)):
                        list1.append(word2[i+j])
                    break
            return "".join(list1)