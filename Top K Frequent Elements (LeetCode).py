import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=Counter(nums)
        dict1 = dict( sorted(nums.items(), key=operator.itemgetter(1),reverse=True))
        count1=0
        list1=[]
        for i,j in dict1.items():
            list1.append(i)
            count1+=1
            if count1==k:
                break
        return list1