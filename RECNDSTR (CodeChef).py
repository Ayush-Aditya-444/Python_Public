# cook your dish here
for _ in range(int(input())):
    str1=input()
    if len(set(str1))==1:
        print("YES")
    else:
        Lstr1=""
        Rstr1=""
        for i in range(len(str1)):
            int1=(i+1)%len(str1)
            Rstr1+=str1[int1]
        for j in range(len(str1)):
            int1=(j-1)%len(str1)
            Lstr1+=str1[int1]
        if Lstr1==Rstr1:
            print("YES")
        else:
            print("NO")