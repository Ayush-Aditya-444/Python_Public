class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        list1=items1+items2
        list2=[]
        dict1={}
        for i in range(len(list1)):
            if list1[i][0] in dict1:
                dict1[list1[i][0]]+=list1[i][1]
            else:
                dict1[list1[i][0]]=list1[i][1]
        for key,values in dict1.items():
            list2.append([key,values])
        return sorted(list2)