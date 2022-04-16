class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1=[]
        a=0
        for i in range(len(nums)):
            if i%2==0:
                list1.append(nums[a])
                a+=1
            else:
                list1.append(nums[n])
                n+=1
        return list1