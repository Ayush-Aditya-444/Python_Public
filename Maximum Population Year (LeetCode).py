class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dict1 = {}
        for i in logs:
            for i in range(i[0] , i[1]):
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
        max1 = -1
        year = -1
        for i in dict1:
            if dict1[i] > max1:
                max1 = dict1[i]
                year = i
            elif dict1[i] == max1 and year > i:
                year = i
        return year