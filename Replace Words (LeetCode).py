class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split()
        for i in range(len(s)):
            for j in range(len(dictionary)):
                str2=s[i]
                str1=dictionary[j]+str2[len(dictionary[j]):]
                if str1==s[i]:
                    s[i]=dictionary[j]
        return " ".join(s)