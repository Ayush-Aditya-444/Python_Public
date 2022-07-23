class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        min_dist=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    min_dist +=1
                    break
        return len(arr1)-(min_dist)