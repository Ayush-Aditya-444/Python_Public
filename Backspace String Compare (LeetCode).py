class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list1=[]
        list2=[]
        for i in range(len(s)):
            if ord("a")<=ord(s[i]) and ord("z")>=ord(s[i]):
                list1.append(s[i])
            else:
                if list1:
                    list1.pop()
        for j in range(len(t)):
            if ord("a")<=ord(t[j]) and ord("z")>=ord(t[j]):
                list2.append(t[j])
            else:
                if list2:
                    list2.pop()
        if list1==list2:
            return True
        else:
            return False