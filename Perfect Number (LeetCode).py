class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        list = [6, 28, 496, 8128, 33550336]
        return (num in list)