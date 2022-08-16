class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            sum1=0
            count1=start-1
            while count1!=destination-1:
                sum1+=distance[count1]
                count1-=1
            sum2=sum(distance)-sum1
        else:
            sum1=0
            for i in range(start,destination):
                sum1+=distance[i]
            sum2=sum(distance)-sum1
        if sum1>sum2:
            return sum2
        else:
            return sum1
        