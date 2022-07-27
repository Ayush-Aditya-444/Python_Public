class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        list1=[]
        nums.sort()
        for i in range(len(nums)):
            if sum(list1)<=sum(nums):
                a=nums.pop()
                list1.append(a)
            else:
                break
        return list1