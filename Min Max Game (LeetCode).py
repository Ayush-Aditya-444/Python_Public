class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums)==1:
                    return nums[0]

        #as long as my length doesn't become 1, I repeat the process
        while len(nums)!=1:
            #we take a newnums everytime of size n//2
            newnums = [-1]*(len(nums)//2)
            for i in range(0,len(nums)//2):
                if i%2==0:
                    newnums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newnums[i] = max(nums[2 * i], nums[2 * i + 1])
            #add the newarray to the older one.
            nums = newnums

        return nums[0]