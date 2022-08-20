class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count1=0
        count2=0
        s=list(word)
        for i in range(len(word)):
            if s[i].islower():
                count1+=1
            else:
                count2+=1
        if count1==len(s) or count2==len(s):
            return True
        elif count2==1 and count1==len(s)-1 and s[0].isupper():
            return True
        else:
            return False