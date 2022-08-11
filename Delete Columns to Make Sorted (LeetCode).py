class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count1=0
        for i in range(len(strs[0])):
            list1=[]
            for j in range(len(strs)):
                list1.append(strs[j][i])
            if list1!=sorted(list1):
                count1+=1
        return count1