class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word=list(word)

        list1=[]
        str1=""
        for i in range(len(word)):
            try:
                if word[i].isnumeric():
                    str1+=word[i]
                    if word[i+1].isnumeric()==False:
                        list1.append(int(str1))
                        str1=""
            except IndexError:
                list1.append(int(str1))
        return len(set(list1))
                        