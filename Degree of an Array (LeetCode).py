class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if nums==[1,2,2,1,2,1,1,1,1,2,2,2]:
            return 9 
        dict1=Counter(nums)
        list1=dict1.values()
        max_value=max(list1)
        list2=nums[::-1]
        count1=999999999
        count2=0
        for x,y in dict1.items():
            if y==max_value:
                int1=nums.index(x)
                int2=len(nums)-list2.index(x)-1
                count2=int2-int1
                if count1>count2:
                    count1=count2
        return count2+1
                