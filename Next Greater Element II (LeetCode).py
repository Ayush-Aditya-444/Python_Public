class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a=len(nums)
        nums=nums+nums
        stack=[]
        a=max(nums)
        for i in range(len(nums)//2):
            if nums[i]==a:
                stack.append(-1)
            else:
                for j in range(i+1,len(nums)):
                    if nums[i]<nums[j]:
                        stack.append(nums[j])
                        break
        return stack