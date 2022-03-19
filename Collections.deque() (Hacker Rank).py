from collections import deque
d=deque()
N=int(input())
for i in range(N):
    A=list(input().split())
    if A[0]=='append':
        d.append(int(A[1]))
    elif A[0]=='appendleft':
        d.appendleft(int(A[1]))
    elif A[0]=='pop':
        d.pop()
    elif A[0]=='popleft':
        d.popleft()
print(*d)