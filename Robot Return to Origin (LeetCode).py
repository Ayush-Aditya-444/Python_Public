class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves=list(moves)
        count1=0
        count2=0
        count3=0
        count4=0
        for i in range(len(moves)):
            if "U"==moves[i]:
                count1+=1
            elif "D"==moves[i]:
                count2+=1
            elif "L"==moves[i]:
                count3+=1
            else:
                count4+=1
        if count4==count3 and count2==count1:
            return True
        return False