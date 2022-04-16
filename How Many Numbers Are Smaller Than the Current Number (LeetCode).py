class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=0
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    a+=1
                else:
                    continue
            list1.append(a)
            a=0
        return list1         