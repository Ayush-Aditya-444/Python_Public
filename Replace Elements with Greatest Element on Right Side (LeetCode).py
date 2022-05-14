class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        list1=[]
        for i in range(1,len(arr)):
            list1.append(max(arr[i:]))
        list1.append(-1)
        return list1