class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=current.split(":")
        correct=correct.split(":")
        int1=(60*int(current[0]))+int(current[1])
        int2=(60*int(correct[0]))+int(correct[1])
        count1=0
        count2=abs(int1-int2)
        while count2>4:
            if count2>=60:
                count1+=1
                count2-=60
            elif count2>=15:
                count1+=1
                count2-=15
            elif count2>=5:
                count1+=1
                count2-=5
        return count1+count2