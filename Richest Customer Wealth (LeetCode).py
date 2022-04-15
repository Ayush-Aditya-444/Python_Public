class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=0
        for i in accounts:
            if a<sum(i):
                a=sum(i)
        return a