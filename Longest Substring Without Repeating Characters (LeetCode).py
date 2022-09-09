class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s))==1:
            return 1
        count1=0
        for i in range(len(s)):
            str1=s[i:]
            list1=[]
            count2=0
            for j in range(len(str1)):
                if str1[j] not in list1:
                    list1.append(str1[j])
                    count2+=1
                else:
                    if count2>count1:
                        count1=count2
                    break
            if count2>count1:
                count1=count2
        return count1
                    