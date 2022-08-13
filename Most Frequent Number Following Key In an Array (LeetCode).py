class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        list1=[]
        dict1={}
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] in dict1:
                    dict1[nums[i+1]]+=1
                else:
                    dict1[nums[i+1]]=1
        sum1=0
        count1=0
        for x,y in dict1.items():
            if sum1<y:
                count1=x
                sum1=y
        return count1
