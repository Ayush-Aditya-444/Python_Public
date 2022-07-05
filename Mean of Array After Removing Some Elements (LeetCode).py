class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        count1=len(arr)
        starting_5per=(len(arr)*5)//100
        ending_5per=(len(arr)*95)//100
        sum1=sum(arr[starting_5per:ending_5per])
        return sum1/(count1-2*starting_5per)
            
        