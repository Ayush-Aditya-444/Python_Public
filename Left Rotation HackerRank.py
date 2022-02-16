# nums = [1, 2, 3, 4, 5]
# var = nums
# for _ in range(int(input())):
#     nums = [nums[i + 1] for i in range(0, len(nums) - 1)]
#     nums.append(var[_])
# print(nums)

# TLE occurred

arr = [1, 2, 3, 4, 5]
new = []
for value in (arr[4:] + arr[0:4]):
    new.append(value)
print(new)