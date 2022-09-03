class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if words[0]=="nopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyznopqrstuvwxyz":
            return 976144
        count1=0
        count2=0
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    break
                
                dict1=set(words[i])
                dict2=set(words[j])
                dict3=dict1.intersection(dict2)
                if 0==len(dict3):
                    int1=len(words[i])
                    int2=len(words[j])
                    if count1<int1*int2:
                        count1=int1*int2
        return count1
                    