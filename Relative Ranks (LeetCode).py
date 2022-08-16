class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score)==1:
            list1=["Gold Medal"]
            return list1
        elif len(score)==2:
            if score[0]>score[1]:
                list1=["Gold Medal","Silver Medal"]
                return list1
            else:
                list1=["Silver Medal","Gold Medal"]
                return list1
        else:
            list1=sorted(score)
            list1=list1[::-1]
            list2=[]
            for i in range(len(list1)):
                if score[i]==list1[2]:
                    list2.append("Bronze Medal")
                elif score[i]==list1[1]:
                    list2.append("Silver Medal")
                elif score[i]==list1[0]:
                    list2.append("Gold Medal")
                else:
                    int1=list1.index(score[i])
                    list2.append(str(int1+1))
            return list2