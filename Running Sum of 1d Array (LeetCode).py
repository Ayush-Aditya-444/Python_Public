class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1=[]
        a=0
        for i in range(len(nums)):
            a=a+nums[i]
            list1.append(a)
        return list1
            