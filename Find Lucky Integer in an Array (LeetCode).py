class Solution:
    def findLucky(self, arr: List[int]) -> int:
        list1=[]
        for i in range(len(arr)):
            if arr[i]==arr.count(arr[i]):
                list1.append(arr[i])
        if len(list1)==0:
            return -1
        return max(list1)
