#User function Template for python3
def commonElements (A, B, C):
    # your code here
    count1=0
    count2=0
    count3=0
    list1=[]
    while count1<len(A) and count2<len(B) and count3<len(C):
        if A[count1]==B[count2]==C[count3] and A[count1] not in list1:
            list1.append(A[count1])
            count1+=1
            count2+=1
            count3+=1
        else:
            int1=min(A[count1],B[count2],C[count3])
            if A[count1]==int1:
                count1+=1
            elif B[count2]==int1:
                count2+=1
            else:
                count3+=1
    return list1
A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(commonElements(A,B,C))

