class Solution:
    def countLargestGroup(self, n: int) -> int:
        list1=[]
        for i in range(1,n+1):
            str1=str(i)
            str1=list(str1)
            sum1=0
            for i in range(len(str1)):
                sum1+=int(str1[i])
            list1.append(sum1)
        dict1=Counter(list1)
        max1 = dict1.values()
        max2 = max(max1)
        count1=0
        for i,j in dict1.items():
            if j==max2:
                count1+=1
        return count1
        