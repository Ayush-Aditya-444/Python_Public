for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[0] + nums[1])
