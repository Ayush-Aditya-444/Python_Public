class Solution:
    def freqAlphabets(self, s: str) -> str:
        a="abcdefghijklmnopqrstuvwxyz"
        stack=[]
        i=0
        while i<len(s):
            try:
                if s[i].isnumeric():
                    if s[i+2]=="#":
                        z=int(s[i:i+2])
                        stack.append(a[z-1])
                        i+=3
                    else:
                        stack.append(a[int(s[i])-1])
                        i+=1
            except IndexError:
                    stack.append(a[int(s[i])-1])
                    i+=1
        return "".join(stack)
        