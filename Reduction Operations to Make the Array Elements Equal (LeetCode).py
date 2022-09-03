class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        else:
            nums.sort(reverse=True)
            int1=nums[-1]
            dict1=Counter(nums)
            count1=0
            count2=0
            for i,j in dict1.items():
                if i!=int1:
                    count1=count1+j
                    count2=count2+count1
            return count2