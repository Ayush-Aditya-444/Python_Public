class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            try:
                if arr[i]<arr[i+1] and i==len(arr)-1:
                    return False
                elif arr[i]<arr[i+1]:
                    continue
                elif arr[i]>arr[i+1] and i==0:
                    return False
                elif arr[i]>arr[i+1]:
                    a=i
                    break
                else:
                    return False
            except IndexError:
                return False
        for j in range(a,len(arr)):
            try:
                if arr[j]>arr[j+1] and j==len(arr)-1:
                    return True
                elif arr[j]>arr[j+1]:
                    continue
                else:
                    return False
            except IndexError:
                return True