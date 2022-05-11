from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        list2=deque([])
        for i in range(len(nums)):
            if nums[i]%2!=0:
                list2.append(nums[i])
            else:
                list2.appendleft(nums[i])
        return list2