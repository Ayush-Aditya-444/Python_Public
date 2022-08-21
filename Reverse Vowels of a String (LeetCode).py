class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        str1="aeiouAEIOU"
        count1=0
        count2=len(s)-1
        while count2>count1:
            try:
                if s[count1] not in str1 and s[count2] not in str1:
                    count1+=1
                    count2-=1
                elif s[count1] in str1:
                    if s[count2] not in str1:
                        count2-=1
                    else:
                        s[count1],s[count2]=s[count2],s[count1]
                        count1+=1
                        count2-=1
                else:
                    if s[count1] not in str1:
                        count1+=1
                    else:
                        s[count1],s[count2]=s[count2],s[count1]
                        count1+=1
                        count2-=1
            except IndexError:
                break
        return "".join(s)