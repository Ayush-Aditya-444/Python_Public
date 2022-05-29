class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        list1=[]
        for i in nums:
            if i not in list1:
                list1.append(i)
        list1.sort()
        if len(list1)<3:
            return list1[-1]
        else:
            return list1[-3]