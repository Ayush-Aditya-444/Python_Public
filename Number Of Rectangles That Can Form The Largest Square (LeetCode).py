class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []
        count = 0
        for i in rectangles:
            arr.append(min(i))
        for j in range(len(arr)):
            if arr[j] == max(arr):
                count+=1
        return count