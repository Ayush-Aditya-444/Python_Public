class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=num1.split("+")
        num2=num2.split("+")
        int1=int(num1[0])
        str1=num1[1]
        int2=int(str1[:len(str1)-1])
        int3=int(num2[0])
        str2=num2[1]
        int4=int(str2[:len(str2)-1])
        int5=int1*int3
        int6=int1*int4
        int7=int2*int3
        int8=-(int2*int4)
        int9=str(int5+int8)
        int10=str(int6+int7)+"i"
        return int9 + "+" + int10
