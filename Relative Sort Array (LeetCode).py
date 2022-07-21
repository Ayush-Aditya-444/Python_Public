class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1=[]
        list2=[]
        for i in range(len(arr2)):
            a=arr1.count(arr2[i])
            for j in range(a):
                list1.append(arr2[i])
        for i in range(len(arr1)):
            if arr1[i] not in list1:
                list2.append(arr1[i])
        list2.sort()
        return list1+list2