class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
            s1=s1.split()
            s2=s2.split()
            list1=s1+s2
            dict1={}
            for i in range(len(list1)):
                if list1[i] in dict1:
                    dict1[list1[i]]+=1
                else:
                    dict1[list1[i]]=1
            list2=[]
            for i,j in dict1.items():
                if j==1:
                    list2.append(i)
            return list2
                    
            
        