class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            list1.append(i+1)
        list1=set(list1)
        nums=set(nums)
        list1=list1.difference(nums)
        return list1