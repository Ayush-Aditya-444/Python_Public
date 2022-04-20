t=int(input())
for i in range(t):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	a=0
	flag=True
	for i in range(len(l)):
		if(l[i]>=m):
			a+=l[i]-m
		elif(a+l[i]>=m):
			a+=l[i]-m
		else:
			flag=False
			break
	if flag:
		print("YES")
	else:
		print("NO",i+1)