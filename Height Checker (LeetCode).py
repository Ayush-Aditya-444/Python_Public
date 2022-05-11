class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        list1=heights
        list1=sorted(list1)
        count1=0
        for i in range(len(list1)):
            if list1[i]!=heights[i]:
                count1+=1
        return count1