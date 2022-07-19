for _ in range(int(input())):
    input_num=int(input())
    input_str1=["a","e","i","o","u"]
    str1=input()
    str1=list(str1)
    p=1
    count1=0
    for i in range(len(str1)):
        if str1[i] not in input_str1:
            count1+=1
            if count1==4:
                p=0
                print("NO")
                break
        elif str1[i] in input_str1:
            count1=0
    if p==1:
        print("YES")