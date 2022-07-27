class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            list1.append(nums[i]*nums[i])
        return sorted(list1)