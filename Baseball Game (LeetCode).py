class Solution:
    def calPoints(self, ops: List[str]) -> int:
        list1=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                list1.append(sum(list1[len(list1)-2:]))
            elif ops[i]=="C":
                list1.pop()
            elif ops[i]=="D":
                list1.append(list1[-1]*2)
            else:
                list1.append(int(ops[i]))
        return sum(list1)