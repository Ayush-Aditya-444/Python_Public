class Solution:
    def minSwaps(self, s: str) -> int:
        max_count=0 
        count1=0
        for i in range(len(s)):
            if s[i]=="]":
                count1+=1
                max_count = max(max_count, count1)
            else:
                count1-=1
        return (max_count+1)//2