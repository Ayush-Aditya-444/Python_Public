class Solution:
    def interpret(self, command: str) -> str:
        command=list(command)
        stack=[]
        for i in range(len(command)):
            if command[i]=="(":
                if command[i+1]==")":
                    stack.append("o")
            else:
                stack.append(command[i])
                if stack[-1]=="(" or stack[-1]==")":
                    stack.pop()
        return "".join(stack)