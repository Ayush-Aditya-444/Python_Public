class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        int1=len(candyType)//2
        list1=set(candyType)
        if int1<len(list1):
            return int1
        else:
            return len(list1)