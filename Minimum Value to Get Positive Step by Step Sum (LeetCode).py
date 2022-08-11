class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        count1=0
        count3=0
        while count1!=len(nums):
            count1=0
            count3+=1
            count2=count3
            for i in range(len(nums)):
                count2+=nums[i]
                if count2>0:
                    count1+=1
        return count3