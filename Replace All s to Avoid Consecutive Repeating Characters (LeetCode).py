class Solution:
    def modifyString(self, s: str) -> str:
        if s=="?":
            return "a"
        s=list(s)
        for i in range(len(s)):
            if s[i]=='?':
                for j in 'abc':
                    if i==0 and s[i+1]!=j:
                        s[i]=j
                        break
                    if i==len(s)-1 and s[i-1]!=j:
                        s[i]=j
                        break
                    if (i>0 and i<len(s)-1) and s[i-1]!=j and s[i+1]!=j: 
                        s[i]=j
                        break
        return ''.join(s)