class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        if len(words1)>len(words2):
            count1=0
            for i in words2:
                if words2.count(i)==1:
                    if i in words1:
                        if words1.count(i)==1:
                            count1+=1
            return count1
        else:
            a=len(words1)
            count1=0
            for i in words1:
                if words1.count(i)==1:
                    if i in words2:
                        if words2.count(i)==1:
                            count1+=1
            return count1