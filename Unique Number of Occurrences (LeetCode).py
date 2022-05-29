class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        list1=list(set(arr))
        list2=[]
        for i in range(len(list1)):
            list2.append(arr.count(list1[i]))
        if len(set(list2))==len(list2):
            return True
        else:
            return False