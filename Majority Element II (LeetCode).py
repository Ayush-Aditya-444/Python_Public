class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        int1=len(nums)//3
        dict1=Counter(nums)
        list1=[]
        for i,j in dict1.items():
            if int1<j:
                list1.append(i)
        return list1