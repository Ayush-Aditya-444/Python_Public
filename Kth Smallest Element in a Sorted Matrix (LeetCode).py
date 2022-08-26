class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        list1=[]
        for i in range(len(matrix)):
            list1+=matrix[i]
        list1=sorted(list1)
        return list1[k-1]