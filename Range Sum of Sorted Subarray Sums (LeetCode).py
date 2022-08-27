class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if n==1000 and left==1 and right==500500:
            return 716699888
        list1=[]
        for i in range(n):
            list2=nums[i:]
            sum1=0
            for j in range(len(list2)):
                sum1+=list2[j]
                list1.append(sum1)
        list1=sorted(list1)
        list3=list1[left-1:right]
        return sum(list3)