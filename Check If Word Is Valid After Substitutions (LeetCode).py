class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        if s.count("a")==s.count("b") and s.count("b")==s.count("c"):
            stack=[]
            for i in range(len(s)):
                stack.append(s[i])
                try:
                    if stack[-1]=="c":
                        stack.pop()
                        if stack[-1]=="b":
                            stack.pop()
                            if stack[-1]=="a":
                                stack.pop()
                except IndexError:
                    return False
            if stack:
                return False
            else:
                return True
        else:
            return False