class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            list1.append(nums[nums[i]])
        return list1