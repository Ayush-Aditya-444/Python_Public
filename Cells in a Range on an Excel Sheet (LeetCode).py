class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        count1=int(s[1])
        count2=int(s[4])+1
        stack=[]
        for i in range(ord(s[0]), ord(s[3])+1):
            for j in range(count1, count2):
                stack.append(chr(i)+str(j))
        return stack