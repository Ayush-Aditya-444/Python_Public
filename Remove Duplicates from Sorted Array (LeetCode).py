class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[a]=nums[i]
                a+=1
        nums[a]=nums[-1]
        return a+1