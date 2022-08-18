class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1=Counter(text)
        return min(dict1["b"],dict1["a"],dict1["l"]//2,dict1["o"]//2,dict1["n"])