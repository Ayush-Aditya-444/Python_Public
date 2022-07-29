from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        t = min(list(d.values()))
        if t==1:
            return False
        for i in range(2, t+1):
            m = True
            for x in list(d.values()):
                if x%i!=0:
                    m = False
            if m==True:
                return True
        return False