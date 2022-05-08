class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for i in image:
            i.reverse()
            result.append(1 - x for x in i)
        return result