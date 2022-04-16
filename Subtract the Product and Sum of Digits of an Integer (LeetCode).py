class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1 = [int(i) for i in str(n)]
        b=1
        for j in range(len(list1)):
            b=b*list1[j]
        c=b-sum(list1)
        return c
        