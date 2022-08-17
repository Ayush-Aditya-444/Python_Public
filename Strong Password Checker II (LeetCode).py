class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        s=list(password)
        if len(s)<8:
            return False
        a={"!","@","#","$","%","^","&","*","(",")","-","+"}
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        for i in range(len(s)):
            if s[i].islower():
                count1+=1
            if s[i].isupper():
                count2+=1
            if s[i].isnumeric():
                count3+=1
            if s[i] in a:
                count4+=1
            try:
                if s[i+1]==s[i]:
                    return False
            except IndexError:
                break
        if count1!=0 and count2!=0 and count3!=0 and count4!=0:
            return True
        else:
            return False