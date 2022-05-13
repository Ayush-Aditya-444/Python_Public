class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list1=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                list1.append(True)
            else:
                list1.append(False)
        return list1