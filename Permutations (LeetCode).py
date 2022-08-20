class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def ayush(nums):
            if len(nums)==1:
                return [nums[:]]
            list1=[]
            for i in range(len(nums)):
                int1=nums[i]
                list2=nums[:i]+nums[i+1:]
                for j in ayush(list2):
                    list1.append([int1]+j)
            return list1
        a=ayush(nums)
        return a