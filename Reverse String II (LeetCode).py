class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        count1=k
        i=2*count1
        list1=s[:k]
        list1=list1[::-1]
        s=list1+s[k:]
        for i in range(i,len(s),2*k):
            if i%k==0:
                list1=s[i:i+k]
                list1=list1[::-1]
                s=s[:i]+list1+s[i+k:]
        return "".join(s)