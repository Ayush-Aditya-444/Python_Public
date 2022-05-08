for _ in range(int(input())):
    length_str1=int(input())
    str1=input()
    str2=input()
    if sorted(str1)==sorted(str2):
        print("YES")
    else:
        print("NO")