class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        list1=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                s[i]=int(s[i])
                list1.append(s[i])
        for i in range(len(list1)-1):
            if list1[i]>=list1[i+1]:
                return False
        return True