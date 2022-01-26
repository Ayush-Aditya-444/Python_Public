n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
for i in range(len(arr)):
    if arr[i]==arr[i+1]:
        pass
    else:
        print(arr[i+1])
        break