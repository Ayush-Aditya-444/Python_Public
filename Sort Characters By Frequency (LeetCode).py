import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        s=Counter(s)
        dict1 = dict( sorted(s.items(), key=operator.itemgetter(1),reverse=True))
        str1=""
        for i,j in dict1.items():
            for k in range(j):
                str1+=i
        return str1
        