class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        int1=customers[0][1]
        int2=customers[0][0]+customers[0][1]
        for i in range(1,len(customers)):
            if int2<customers[i][0]:
                int2=customers[i][0]+customers[i][1]
                int1+=customers[i][1]
            else:
                int2+=customers[i][1]
                int1+=int2-customers[i][0]
        return int1/len(customers)
            
        