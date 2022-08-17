class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count1=-1
        for i in range(len(s)//2):
            s[i],s[count1]=s[count1],s[i]
            count1-=1