class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target not in letters:
            letters.append(target)
            list1=sorted(list(set(letters)))
            int1=list1.index(target)
            if int1!=len(list1)-1:
                return list1[int1+1]
            else:
                return list1[0]
        else:
            letters=sorted(list(set(letters)))
            int1=letters.index(target)
            if int1!=len(letters)-1:
                return letters[int1+1]
            else:
                return letters[0]