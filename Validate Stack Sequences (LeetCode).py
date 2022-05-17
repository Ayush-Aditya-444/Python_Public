class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
            stack=[]
            b=0
            for i in range(len(pushed)):
                stack.append(pushed[i])
                while True:
                    try:
                        if stack[-1]==popped[b]:
                            stack.pop()
                            b+=1
                        else:
                            break
                    except IndexError:
                        break
            for i in range(len(stack)):
                if stack[-1]==popped[b]:
                    stack.pop()
                    b+=1
                else:
                    return False
                    break
            if not stack:
                return True