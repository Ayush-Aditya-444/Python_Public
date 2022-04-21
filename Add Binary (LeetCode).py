class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binaryToDecimal1(a):
            return int(a,2)
        def binaryToDecimal2(b):
            return int(b,2)
        def decimalToBinary1(e):
            return "{0:b}".format(int(e))
        c=binaryToDecimal1(a)
        d=binaryToDecimal2(b)
        e=c+d
        f=decimalToBinary1(e)
        return str(f)