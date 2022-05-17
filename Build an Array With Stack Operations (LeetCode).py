class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        list1=[]
        num1=min(max(target),n)
        for i in range(1,num1+1):
            list1.append(i)
            if list1[-1] in target:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")
        return stack