class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0,0)
        count1=0
        count2=0
        keysPressed=list(keysPressed)
        for i in range(len(releaseTimes)-1):
            int1=releaseTimes[i+1]-releaseTimes[i]
            int2=ord(keysPressed[i])
            if count1<int1:
                count1=int1
                count2=int2
            elif count1==int1:
                if count2<int2:
                    count2=int2
        str1=chr(count2)
        return str1
                