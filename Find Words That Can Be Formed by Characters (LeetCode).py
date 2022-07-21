class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum1=0
        chars=list(chars)
        for i in range(len(words)):
            a=list(words[i])
            b=chars.copy()
            count1=0
            for j in range(len(a)):
                if a[j] in b:
                    count1+=1
                    b.remove(a[j])
                    if count1==len(a):
                        sum1+=len(a)
        return sum1