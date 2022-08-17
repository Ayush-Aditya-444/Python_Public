class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        count1=0
        for i in range(len(text)):
            count2=0
            for j in range(len(text[i])):
                if text[i][j] not in brokenLetters:
                    count2+=1
                    if count2==len(text[i]):
                        count1+=1
        return count1
                
        