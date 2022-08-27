class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=Counter(s)
        t=Counter(t)
        dict1=s | t
        count1=0
        for i,j in dict1.items():
            if i not in s:
                count1+=j
            elif dict1[i]>s[i]:
                int1=dict1[i]-s[i]
                count1+=int1
        for i,j in dict1.items():
            if i not in t:
                count1+=j
            elif dict1[i]>t[i]:
                int1=dict1[i]-t[i]
                count1+=int1
        return count1