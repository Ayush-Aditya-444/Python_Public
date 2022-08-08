class Solution:
    def findLHS(self, nums):
        res = 0
        counter = Counter(nums)
    
        for c in counter:
            if c+1 in counter:
                res = max(res, counter[c] + counter[c+1])
        
        return res