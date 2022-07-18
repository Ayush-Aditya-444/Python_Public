class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        count1=0
        count2=0
        count3=0
        list1=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(nums)):
            if count1%2==0:
                list1.append(even[count2])
                count2+=1
                count1+=1
            else:
                list1.append(odd[count3])
                count3+=1
                count1+=1
        return list1
                
            