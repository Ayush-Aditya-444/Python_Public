class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''.join([str(elem) for elem in digits])
        a=int(a)
        a+=1
        x = [int(a) for a in str(a)]
        return x