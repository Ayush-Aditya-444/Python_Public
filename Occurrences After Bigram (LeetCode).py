class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text=text.split()
        list1=[]
        for i in range(len(text)-2):
            if first==text[i]:
                if second==text[i+1]:
                    list1.append(text[i+2])
        return list1
                    