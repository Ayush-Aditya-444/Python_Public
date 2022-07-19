class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a=0
        list1=[]
        arr.sort()
        a=1000000000000000
        for i in range(len(arr)-1):
            z=arr[i+1]
            y=arr[i]
            b=z-y
            if a>b:
                list1.clear()
                list1.append([arr[i],arr[i+1]])
                a=b            
            elif a==b:
                list1.append([arr[i],arr[i+1]])
        return list1