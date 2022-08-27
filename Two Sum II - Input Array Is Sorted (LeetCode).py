class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            int1=target-numbers[i]
            count1=i+1
            count2=len(numbers)-1
            while count1<=count2:
                mid=(count1+count2)//2
                if numbers[mid]==int1:
                    return sorted([mid+1,i+1])
                else:
                    if numbers[mid]<int1:
                        count1=mid+1
                    else:
                        count2=mid-1