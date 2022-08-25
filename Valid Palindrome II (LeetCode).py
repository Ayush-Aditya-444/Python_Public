class Solution:
    def validPalindrome(self,s):
        if s==s[::-1]:
            return True
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                list1=(s[:i]+s[i+1:])
                if list1==list1[::-1]:
                    return True
                list2=(s[:j]+s[j+1:])
                if list2==list2[::-1]:
                    return True
                return False