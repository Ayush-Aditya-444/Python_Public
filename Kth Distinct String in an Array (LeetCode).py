class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        try:
            list1=[]
            for i in arr:
                if arr.count(i)==1:
                    list1.append(i)
            return list1[k-1]
        except IndexError:
            return ""
            