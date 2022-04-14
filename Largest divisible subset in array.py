def findLargest(arr, n):
    arr.sort(reverse = False)
    divCount = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    max_ind = 0
    for i in range(1,n):
        for j in range(i):
            if (arr[i] % arr[j] == 0):
                if (divCount[i] < divCount[j] + 1):
                    divCount[i] = divCount[j]+1
                    prev[i] = j
        if (divCount[max_ind] < divCount[i]):
            max_ind = i
    k = max_ind
    while (k >= 0):
        print(arr[k],end = " ")
        k = prev[k]
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = len(arr)
    findLargest(arr, n)