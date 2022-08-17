class Solution:
    def minTimeToType(self, word: str) -> int:
        str1="abcdefghijklmnopqrstuvwxyz"
        str1=deque(str1)
        word=list(word)
        count1=str1.index(word[0])
        if count1>13:
            count1=26-count1
        for i in range(len(word)-1):
            int1=str1.index(word[i+1])
            int2=str1.index(word[i])
            int3=abs(int2-int1)
            if int3>=13:
                int3=26-int3
                count1+=int3
            else:
                count1+=int3
        return count1+len(word)