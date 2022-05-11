class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        list1=[]
        if target in nums:
            a=nums.index(target)
            b=nums.count(target)
            for i in range(b):
                list1.append(a)
                a+=1
            return list1
        else:
            return list1