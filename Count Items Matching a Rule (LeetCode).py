class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        d = {'type':0,'color':1,'name':2} 
        c = 0                             
        index = d[ruleKey]                
        for item in items:               
            if item[index] == ruleValue:  
                c += 1                    
        return c          