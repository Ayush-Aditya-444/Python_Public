class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=Counter(ransomNote)
        dict2=Counter(magazine)
        for i,j in dict1.items():
            str1=i
            if dict1[str1]>dict2[str1]:
                return False
        return True
            