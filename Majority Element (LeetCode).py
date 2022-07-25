class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set1=list(set(nums))
        int1=0
        list1=[]
        for i in range(len(set1)):
            if nums.count(set1[i])>=int1:
                list1.clear()
                list1.append(set1[i])
                int1=nums.count(set1[i])
                
        return list1[0]