from itertools import permutations
def ayush(nums):
        list1=permutations(nums,4)
        count1=0
        for i in list(list1):
            if i[0]*i[1]==i[2]*i[3]:
                count1+=1
        return count1
nums = [2,3,4,6]
print(ayush(nums))