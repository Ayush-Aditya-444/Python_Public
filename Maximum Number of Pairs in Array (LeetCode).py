class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        set1=set(nums)
        set1=list(set1)
        pair=0
        left=0
        list1=[]
        for i in range(len(set1)):
            a=nums.count(set1[i])
            if a%2==0:
                pair+=(a//2)
            else:
                pair+=(a//2)
                left+=1
        list1.append(pair)
        list1.append(left)
        return list1
            