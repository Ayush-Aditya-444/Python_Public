class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        int1=0
        int2=0
        a=nums.count(nums[0])
        b=nums.count(nums[-1])
        if len(nums)<=2:
            return 0
        if len(nums)-a-b<1:
            return 0
        return len(nums)-a-b
        