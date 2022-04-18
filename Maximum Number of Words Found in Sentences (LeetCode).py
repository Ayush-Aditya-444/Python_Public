class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        list1=[]
        for i in sentences:
            a=i.split()
            list1.append(len(a))
        return max(list1)