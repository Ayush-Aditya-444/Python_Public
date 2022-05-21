class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stack=[]
        for i in range(1,n+1):
            stack.append(i)
        count1=0
        while len(stack)>1:
            i=abs(i+k-1)%len(stack)
            stack.pop(i)
        return stack[0]
        