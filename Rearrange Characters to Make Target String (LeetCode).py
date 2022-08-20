class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        list1=[]
        for i in range(len(target)):
            int1=s.count(target[i])
            int2=target.count(target[i])
            if int1>=int2:
                list1.append(int1//int2)
            else:
                return 0
        return min(list1)