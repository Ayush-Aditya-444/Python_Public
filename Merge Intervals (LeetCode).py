class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        list1=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] in range(start,end+1):
                if intervals[i][1]>end:
                    end=intervals[i][1]
            else:
                list1.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        list1.append([start,end])
        return list1