class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict1 = words[0]
        for i in range(1,len(words)):
            dict1 = Counter(dict1) & Counter(words[i])
        return list(dict1.elements())