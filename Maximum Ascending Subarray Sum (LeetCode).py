class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum1=0
        list1=[]
        nums.append(nums[-1]+1)
        for i in range(len(nums)):
            try:
                if nums[i]<nums[i+1]:
                    list1.append(nums[i])
                elif nums[i]>nums[i+1]:
                    list1.append(nums[i])
                    sum2=sum(list1)
                    if sum2>sum1:
                        sum1=sum2
                    list1.clear()
                elif nums[i]==nums[i+1]:
                    list1.append(nums[i])
                    sum2=sum(list1)
                    if sum2>sum1:
                        sum1=sum2
                    list1.clear()
            except IndexError:
                sum2=sum(list1)
                if sum2>sum1:
                    sum1=sum2   
        return sum1