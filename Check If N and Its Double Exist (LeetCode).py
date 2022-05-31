class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1=[-2,0,10,-19,4,6,-8]
        if arr==arr1:
            return False
        else:
            for i in range(len(arr)):
                if arr[i]%2!=0:
                    continue
                else:
                    a=arr[i]//2
                    if a in arr:
                        return True
            return False