class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=list(boxes)
        list1=[]
        sum1=0
        for i in range(1,len(boxes)):
            if boxes[i]=="1":
                sum1+=i
        list1.append(sum1)
        for i in range(1,len(boxes)):
            sum1=0
            list2=boxes[:i]
            list3=boxes[i+1:]
            list2=list2[::-1]
            for j in range(len(list2)):
                if list2[j]=="1":
                    sum1+=j+1
            for j in range(len(list3)):
                if list3[j]=="1":
                    sum1+=j+1
            list1.append(sum1)
        return list1