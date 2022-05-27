class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=list(address)
        stack=[]
        for i in range(len(address)):
            if address[i]!=".":
                stack.append(address[i])
            else:
                stack.append("[")
                stack.append(".")
                stack.append("]")
        return "".join(stack)