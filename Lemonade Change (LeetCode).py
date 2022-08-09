class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5=0
        count10=0
        for i in range(len(bills)):
            if bills[i]==5:
                count5+=1
            elif bills[i]==10:
                if count5>0:
                    count5-=1
                    count10+=1
                else:
                    return False
            elif bills[i]==20:
                if count10>0 and count5>0:
                    count10-=1
                    count5-=1
                elif count10<0 and count5<3:
                    return False
                elif count5>=3:
                    count5-=3
                else:
                    return False
        return True