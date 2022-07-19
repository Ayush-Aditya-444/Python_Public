class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        b=arr[1]-arr[0]
        for i in range(len(arr)-1):
            c=arr[i+1]-arr[i]
            if b==c:
                continue
            else:
                return False
                break
        return True