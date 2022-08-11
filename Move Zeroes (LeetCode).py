class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        int1=nums.count(0)
        for i in range(int1):
            nums.remove(0)
            nums.append(0)