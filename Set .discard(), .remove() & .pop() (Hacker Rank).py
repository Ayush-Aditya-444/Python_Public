n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))