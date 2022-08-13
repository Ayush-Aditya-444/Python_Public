class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code=code*2
        list1=[0]
        if k==0:
            return list1*(len(code)//2)
        elif k>0:
            list1=[]
            for i in range(len(code)//2):
                sum1=0
                for j in range(k):
                    sum1+=code[i+j+1]
                list1.append(sum1)
            return list1
        elif k<0:
            list1=[]
            for i in range(len(code)//2):
                sum1=0
                for j in range(abs(k)):
                    sum1+=code[i-j-1]
                list1.append(sum1)
            return list1
            