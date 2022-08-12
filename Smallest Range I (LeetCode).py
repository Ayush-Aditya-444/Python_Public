class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        if (nums[-1]-k)-(nums[0]+k)<=0:
            return 0
        else:
            return (nums[-1]-k)-(nums[0]+k)