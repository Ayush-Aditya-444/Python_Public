class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        count1=0
        if count1 in nums:
            nums.sort()
            int1=nums.index(0)
            int2=min(int1,k)
            for i in range(int2):
                nums[i]=-(nums[i])
        else:
            nums.append(0)
            nums.sort()
            int1=nums.index(0)
            nums.remove(0)
            if k<=int1:
                for i in range(k):
                    nums[i]=-(nums[i])
            else:
                for i in range(int1):
                    nums[i]=-(nums[i])
                int2=k-int1
                nums.sort()
                if int2%2!=0:
                    nums[0]=-(nums[0])
        return sum(nums)