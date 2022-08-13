class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count1=0
        sum1=0
        for i in range(len(arr)):
            int1=arr.count(arr[i])
            if count1<int1:
                count1=int1
                sum1=arr[i]
        return sum1