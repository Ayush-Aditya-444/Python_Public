for i in range(int(input())):
     a,b=map(int,input().split())
     list1=list(map(int,input().split()))
     ans=[]
     for i in range(a-(b-1)):
          ans.append(sum(list1[i:i+b]))
     print(max(ans))