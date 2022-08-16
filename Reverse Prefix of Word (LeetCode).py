class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            word=list(word)
            int1=word.index(ch)
            list1=word[:int1+1]
            list1=list1[::-1]
            list2=word[int1+1:]
            list1=list1+list2
            return "".join(list1)
        except ValueError:
            return "".join(word)
        