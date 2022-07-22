class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        sum1=10000000000
        minmum_index = 1000000000
        for i in range(len(points)):
            int1=points[i][0]
            int2=points[i][1]
            if int1==x or int2==y:
                sum2=abs(int1-x)+abs(int2-y)
                if sum1>sum2:
                    sum1=sum2
                    minmum_index = i
        if sum1 != 10000000000:
            return minmum_index
        else:
            return -1