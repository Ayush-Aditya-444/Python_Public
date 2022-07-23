class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        list3=[]
        for i in range(len(nums)):
            if i%2==0:
                list1.append(nums[i])
            else:
                list2.append(nums[i])
        list1.sort()
        list2.sort(reverse=True)
        count1=0
        count2=0
        for i in range(len(nums)):
            if i%2==0:
                list3.append(list1[count1])
                count1+=1
            else:
                list3.append(list2[count2])
                count2+=1
        return list3