class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left,right = 99999,99999
        for idx in range(start,len(nums)): 
            if nums[idx] == target: 
                left = idx - start 
                break
        for idx in range(start,-1,-1): 
            if nums[idx] == target: 
                right = start - idx 
                break
        return min(left,right)