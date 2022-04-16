class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1=[]
        a=0
        b=1
        for i in range(len(nums)//2):
            c=nums[a]
            d=nums[b]
            for i in range(c):
                list1.append(d)
            a+=2
            b+=2
        return list1