class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dict1=Counter(nums)
        if dict1[0]>=2:
            return [0]*len(nums)
        elif dict1[0]==1:
            product1=1
            count1=0
            list1=[]
            for i in range(0,len(nums)):
                if nums[i]!=0:
                    product1*=nums[i]
                else:
                    count1=i
            list1=[0]*(len(nums)-1)
            list1.insert(count1,product1)
            return list1
        else:
            product1=1
            list1=[]
            for i,j in dict1.items():
                product1*=pow(i,j)
            for i in range(len(nums)):
                int1=product1//nums[i]
                list1.append(int1)
            return list1