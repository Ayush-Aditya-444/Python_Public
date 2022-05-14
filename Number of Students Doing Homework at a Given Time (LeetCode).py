class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count1=0
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                count1+=1
        return count1