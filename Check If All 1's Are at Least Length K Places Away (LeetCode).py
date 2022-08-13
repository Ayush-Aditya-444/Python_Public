class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        list1=[]
        for i in range(len(nums)):
            if nums[i]==1:
                list1.append(i)
        for i in range(len(list1)-1):
            if list1[i+1]-list1[i]-1>=k:
                continue
            else:
                return False
        return True