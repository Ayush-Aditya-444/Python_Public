class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        searchWord=list(searchWord)
        for i in range(len(sentence)):
            count1=0
            list1=list(sentence[i])
            for j in range(len(searchWord)):
                try:
                    if list1[j]==searchWord[j]:
                        count1+=1
                        if count1==len(searchWord):
                            return i+1
                except IndexError:
                    break
        return -1
        