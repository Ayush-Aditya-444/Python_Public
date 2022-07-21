from collections import deque
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        list1=[]
        list2=[]
        list3=[]
        for i in range(len(grid)):
            list1+=grid[i]
        list1=deque(list1)
        for i in range(k):
            a=list1.pop()
            list1.appendleft(a)
        count1=0
        count2=len(grid[0])
        b=[]
        for i in range(len(list1)):
            list2.append(list1[i])
            count1+=1
            if count1%count2==0:
                list3=list2.copy()
                b.append(list3)
                list2.clear()
        return b
        