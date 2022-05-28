class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        z="aeiou"
        y=len(s)//2
        a=s[:y]
        b=s[y:]
        count1=0
        count2=0
        i=0
        while i<len(a):
            if a[i] in z:
                count1+=1
            if b[i] in z:
                count2+=1
            i+=1
        if count1==count2:
            return True
        else:
            return False