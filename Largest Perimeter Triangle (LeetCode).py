class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sum1=0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            int1=nums[i]
            int2=nums[i+1]
            int3=nums[i+2]
            if int1<int2+int3 and int2<int1+int3 and int3<int1+int2:
                sum2=int1+int2+int3 
                if sum1 < sum2:
                    sum1=sum2
        return sum1
        
        