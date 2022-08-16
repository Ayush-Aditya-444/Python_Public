class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict1={}
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                if paths[i][j] not in dict1:
                    dict1[paths[i][j]]=1
                else:
                    dict1[paths[i][j]]+=1
        list1=[]
        for x,y in dict1.items():
            if y==1:
                list1.append(x)
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                if list1[0]==paths[i][j]:
                    if j==0:
                        return list1[1]
                    else:
                        return list1[0]
                    
        