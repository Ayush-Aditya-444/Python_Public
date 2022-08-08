class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        int1=nums.count(val)
        for i in range(int1):
            nums.remove(val)
        return len(nums)