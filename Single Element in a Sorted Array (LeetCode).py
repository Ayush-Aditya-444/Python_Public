class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        for i,j in dict1.items():
            if j==1:
                return i